
# Modules
import joblib
from numpy import sort
import streamlit as st
import pandas as pd
import datetime as dt
import altair as alt


# Load the pre-trained model and data
model = joblib.load('Projects/Store-Sales-Forecasting/rossmann-sales-app/ten_stores_sales_forecasting_model.pkl')
df = pd.read_csv("Projects/Store-Sales-Forecasting/rossmann-sales-app/Model Data/rossman_1_to_10.csv")
df['Date'] = pd.to_datetime(df['Date'])  # Add this line
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Features the model was trained on
trained_on_columns=['Store', 'DayOfWeek', 'Open', 'Promo', 'StateHoliday',
 'SchoolHoliday', 'Month', 'Year']

# Function to build future features for prediction
def build_future_features(store_id, date, is_open, has_promo):
    date = pd.to_datetime(date)

    return pd.DataFrame([{
        'Store': store_id,
        'DayOfWeek': date.dayofweek + 1,
        'Open': 1 if is_open else 0,
        'Promo': 1 if has_promo else 0,
        'StateHoliday': 0,
        'SchoolHoliday': 0,
        'Month': date.month,
        'Year': date.year
    }])


def generate_future_dates(start_date, days):
    start_date = pd.to_datetime(start_date)
    return [start_date + pd.Timedelta(days=i) for i in range(1, days + 1)]

def is_store_open_by_date(date):
    # Rossmann stores are closed on Sunday (DayOfWeek = 7)
    return (date.dayofweek + 1) != 7




# Streamlit App
st.title("Rossmann Store Sale Forecast")

st.header("Welcome to the Rossmann Store Sale Forecast App")

st.write("This app helps you forecast sales for Rossmann stores based on historical data.")

sales_rolling = df.groupby('Date')['Sales'].sum().rolling(window=7).mean()

st.subheader("Explore Historical Data")
col1, col2, col3 = st.columns(3)

with col1:
    data_summary_button = st.button("Data Summary")
with col2:
    first_5rows_button = st.button("First 5 Rows")
with col3:
    sales_overtime_button = st.button("Sales Over Time")

if data_summary_button:
    st.write(df.describe())
if first_5rows_button:
    st.write(df.head(5))
if sales_overtime_button:
    st.line_chart(sales_rolling)

# add user inputs for prediction and let user decide the timeframe of prediction

st.header("Sales Prediction")

st.subheader("Prediction Options")

col_a, col_b = st.columns(2)

with col_a:
    is_open = st.checkbox("Store is Open", value=True)

with col_b:
    has_promo = st.checkbox("Running Promotion", value=False)

st.subheader("Forecast Range")

forecast_days = st.radio(
    "Select forecast horizon:",
    options=[7, 30],
    horizontal=True
)

    
# store_id = st.number_input("Enter Store ID:", min_value=1, max_value=1115, value=1)
store_id = st.selectbox("Select Store ID:", options=[1,2,3,4,5,6,7,8,9,10])

date_input = st.date_input("Select Date for Prediction:", dt.date(2014, 7, 31))

predict_button = st.button("Predict Sales")
col_x, col_y = st.columns(2)

if predict_button:
    # Convert the date_input to match your DataFrame's date format
    if isinstance(date_input, dt.date):
        # Convert to datetime for proper comparison
        
        date_to_find = pd.to_datetime(date_input)
        
        actual_values = df[
            (df['Store'] == store_id) & 
            (df['Date'] > date_to_find) & 
            (df['Date'] < date_to_find + pd.Timedelta(days=forecast_days))
        ][['Date', 'Sales']]
        
        actual_df = pd.DataFrame(actual_values).sort_values(by='Date')
        with col_x:
            st.write(actual_df)


    future_dates = generate_future_dates(date_input, forecast_days)

    predictions = []

    for future_date in future_dates:
        open_status = is_store_open_by_date(future_date)

        features = build_future_features(
            store_id=store_id,
            date=future_date,
            is_open=open_status,
            has_promo=has_promo if open_status else 0
        )

        if not open_status:
            predicted_sales = 0
        else:
            predicted_sales = model.predict(features)[0]


        predicted_sales = model.predict(features)[0]

        predictions.append({
            'Date': future_date,
            'Predicted Sales': predicted_sales
        })

    forecast_df = pd.DataFrame(predictions)

    st.success(f"Forecast for Store {store_id} (next {forecast_days} days)")
    with col_y:
        st.write(forecast_df)

    forecast_df['Type'] = 'Forecast'

    # Prepare actual dataframe (if exists)
    if not actual_df.empty:
        actual_df = actual_df.copy()
        actual_df['Type'] = 'Actual'
        plot_df = pd.concat([
            actual_df[['Date', 'Sales', 'Type']],
            forecast_df.rename(columns={'Predicted Sales': 'Sales'})[['Date', 'Sales', 'Type']]
        ])
    else:
        plot_df = forecast_df.rename(columns={'Predicted Sales': 'Sales'})
        plot_df['Type'] = 'Forecast'
        plot_df['Date'] = plot_df['Date'].dt.date

    chart = alt.Chart(plot_df).mark_line(point=True).encode(
        x=alt.X(
            'Date:T',
            title='Date',
            axis=alt.Axis(format='%d %b %Y',tickCount=forecast_days)

        ),
        y=alt.Y('Sales:Q', title='Sales'),
        color='Type:N',
        tooltip=['Date:T', 'Sales:Q', 'Type:N']
    ).properties(
        title=f"Actual vs Forecast Sales for Store {store_id}"
    )


    st.altair_chart(chart, use_container_width=True)


