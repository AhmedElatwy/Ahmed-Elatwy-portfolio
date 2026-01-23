import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb
from folium.plugins import MarkerCluster
import folium 
from streamlit_folium import st_folium
import os

# Load the model 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@st.cache_resource
def load_model():
    model = xgb.Booster()
    model_path = os.path.join(BASE_DIR, "xgb_model.json")
    model.load_model(model_path)
    return model


@st.cache_resource
def load_model_columns():
    columns_path = os.path.join(BASE_DIR, "model_columns.joblib")
    return joblib.load(columns_path)


model = load_model()
model_columns = load_model_columns()


map_data_path = os.path.join(BASE_DIR, "app_data.csv")
df_map = pd.read_csv(map_data_path)
# --- The Streamlit App ---


st.title("🏡 London Investment Evaluator")


# Build the Map

st.subheader("🗺️ Airbnb Listings Map (Showing up to 500 listings)")

# ---- Session-state guard (IMPORTANT) ----
if "show_map" not in st.session_state:
    st.session_state.show_map = True


def create_map(df_map):
    m = folium.Map(
        location=[51.5074, -0.1278],
        zoom_start=11,
        tiles="CartoDB dark_matter"
    )

    marker_cluster = MarkerCluster().add_to(m)

    for _, row in df_map.sample(min(500, len(df_map))).iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"${row['price']} - {row['room_type']}",
            icon=folium.Icon(
                color="green" if row["price"] < 150 else "red",
                icon="home"
            )
        ).add_to(marker_cluster)

    return m


# ---- Create map ONCE ----
m = create_map(df_map)


# ---- Render map SAFELY ----
if st.session_state.show_map:
    st_folium(
        m,
        width=700,
        height=500,
        key="airbnb_map",
        returned_objects=[]
    )


# User Widgets (The Inputs)
st.sidebar.header("🏷️ Input Property Details")
bedrooms = st.sidebar.slider("Bedrooms", 1, 5, 1)
distance = st.sidebar.number_input("Distance to Center (km)", 0.0, 20.0, 5.0)
room_type = st.sidebar.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
accommodates = st.sidebar.slider("Accommodates", 1, 10, 2)
nights = st.sidebar.slider("Nights", 1, 30, 1)


# The "Prediction Logic" 
st.subheader("💵 Estimated Price Prediction")
if st.sidebar.button("Predict Price"):
    
    # Create a dictionary with the inputs
    input_data = {
        'bedrooms': [bedrooms],
        'distance_to_center': [distance],
        'accommodates': [accommodates], 
        'min_nights': [nights]    
    }
    
    # Create a DataFrame
    input_df = pd.DataFrame(input_data)
    
    # Handle One-Hot Encoding 
    # We add the columns for room_type (setting them to 0 or 1)
    input_df['room_type_Private room'] = 1 if room_type == "Private room" else 0
    input_df['room_type_Shared room'] = 1 if room_type == "Shared room" else 0
    
    # Align with Model Columns
    final_df = pd.DataFrame(columns=model_columns)
    
    # We overwrite the empty columns with our input data
    # Any column we didn't ask for (like 'has_Pool') will remain NaN
    for col in input_df.columns:
        if col in final_df.columns:
            final_df.loc[0, col] = input_df.iloc[0][col]
            
    # Fill missing columns with 0
    final_df.fillna(0, inplace=True)
    
    # --- CONVERT TO DMATRIX (Crucial for JSON models) ---
    data_dmatrix = xgb.DMatrix(final_df)
    
    # Predict
    prediction = model.predict(data_dmatrix)[0]
    
    st.success(f"Estimated Price: ${prediction:.2f}", icon="💰")










