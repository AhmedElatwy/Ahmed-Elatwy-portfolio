# British-Airways-Reviews-Analysis
### Notebook Link : https://www.kaggle.com/code/ahmedealtwy/british-airline-review-analysis
## Overview
This project analyzes customer reviews of British Airways scraped from [AirlineQuality.com](https://www.airlinequality.com/airline-reviews/british-airways/). The goal is to clean, process, and visualize the data to uncover insights about customer satisfaction, trends in ratings over time, and potential areas of improvement for the airline. The dataset includes review titles, ratings, content, and dates, which are processed and visualized using Python libraries like Pandas, Seaborn, and Matplotlib.

## Approach
The project follows these key steps:

1. **Data Collection** (Commented Out in Notebook):
   - The notebook includes a web scraping script (using `requests` and `BeautifulSoup`) to collect reviews from AirlineQuality.com. However, this step is commented out as the dataset was pre-loaded from a CSV file (`airline_reviews.csv`).

2. **Data Cleaning**:
   - **Review Content**: Split the `content` column into `verification` (e.g., "Trip Verified") and `review` text, removing unnecessary icons and prefixes.
   - **Date Formatting**: Converted the `date` column from strings (e.g., "21st February 2025") to a proper datetime format using regex and `pd.to_datetime`.
   - **Verification Correction**: Fixed inconsistencies (e.g., "cNot Verified" to "Not Verified").
   - Checked for null values, duplicates, and outliers; no significant issues were found except for minor rating outliers.

3. **Data Exploration and Visualization**:
   - Used a boxplot (`sns.boxplot`) to visualize the distribution of ratings, identifying potential outliers.
   - Added a 7-day rolling average trend line to track rating changes over time, embedded as a subplot in an infographic saved as `detailed_infographic.png`.

4. **Tools Used**:
   - Python: `pandas` for data manipulation, `seaborn` and `matplotlib` for visualization, `requests` and `BeautifulSoup` for scraping (commented out).
   - Environment: Jupyter Notebook (originally run on Kaggle).

## Conclusion
The analysis successfully cleaned and processed the British Airways review data, revealing the distribution of customer ratings and trends over time. Key findings include:
- Ratings range from 1 to 10, with some outliers on the lower end, suggesting occasional extreme dissatisfaction.
- The 7-day rolling average provides a smoother view of sentiment trends, which could be further explored with more advanced time-series analysis.
- Future work could involve sentiment analysis on the `review` text or correlating ratings with specific flight routes or dates.

  
# Booking Completion Prediction
### Notebook Link : https://www.kaggle.com/code/ahmedealtwy/british-airline-customer-booking-prediction

## Overview
This analysis aims to predict whether customers complete their bookings (0 = No, 1 = Yes) based on a dataset of 50,000 customer booking records, cleaned to 49,281 after removing duplicates. The dataset includes features like number of passengers, sales channel, trip type, and customer preferences (e.g., extra baggage).

## Approach
**Data Source**: Loaded from /kaggle/input/ba-customer-bookings/customer_booking.csv (Kaggle dataset).

**Data Cleaning**:
- Removed 719 duplicate entries, reducing the dataset to 49,281 records.
- Checked for null values
- verified data types (e.g., int64, float64, object).
- Identified outliers in features like purchase_lead (max 867 days) and length_of_stay (max 778 days).
  
## Model Development:
- **Best Model**: XGBoost with scale_pos_weight=3 and n_estimators=100.
- **Training**: Split data into training and test sets (not shown in code but implied in summary).
- **Evaluation Metric**s:
- **Accuracy**: 79% (Test), 78% (Avg Cross-Validation).
- **Yes (1) Metrics**: Precision: 28%, Recall: 28%, F1-Score: 28%.
- **Confusion Matrix**: Identified 353 out of 1,256 "Yes" bookings, missed 903.
- **Feature Importance**: Top predictors include wants_extra_baggage, purchase_lead, and flight_duration.

## Conclusion
Key Findings:
Dataset is imbalanced (85% No, 15% Yes), impacting "Yes" prediction performance.
XGBoost outperforms other models by balancing overall accuracy and "Yes" detection.
