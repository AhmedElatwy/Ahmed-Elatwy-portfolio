# Store Sales Forecasting

## Domain: Retail Operations

[Streamlit Live Web Interface for Real-Time Prediction.](https://rossman-store-sales-forecasting.streamlit.app/)

![Streamlit Live Web Interface for Real-Time Prediction.](Visuals/Streamlit-Full.png)

## Business Problem:
A drugstore chain needed accurate 6-week sales forecasts to optimize inventory and prevent stockouts/overstocking across 1,115 stores.

## My Approach:
o	Conducted Time Series EDA to uncover weekly seasonality (Sunday closures) and the financial impact of promotions.

o	Engineered features for Seasonality (DayOfWeek, Month) and Business Events (Promo, State Holiday).

o	Refinement: Identified and fixed a critical Data Leakage issue (removing the 'Customers' future variable) to ensure the model was realistic for production use.

![Actual vs Prediction](https://github.com/AhmedElatwy/Store-Sales-Forecasting/blob/b8e87807a7fdedac3336be578c2b76f280a7d0e2/Visuals/Actual%20vs%20Prediction.png)

##  Key Results:
o	Quantified that Promotions drive a median sales lift of ~$3,000 per day.

o	Built a Random Forest Regressor achieving a robust R² of ~0.85 (MAE ~$600-800) after removing data leakage.

o	Accurately predicted sales spikes and "Closed Day" drops in the validation set.

## Tech Stack: Python (Scikit-Learn, Random Forest), Time Series Analysis, Feature Engineering.


