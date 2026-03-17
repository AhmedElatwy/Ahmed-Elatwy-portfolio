# Data Analysis Portfolio - Ahmed Elatwy

![Data Analysis](https://img.shields.io/badge/Data-Analysis-blue)
![Python](https://img.shields.io/badge/Python-Expert-green)
![Power BI](https://img.shields.io/badge/Power_BI-Pro-yellow)
![Excel](https://img.shields.io/badge/Excel-Advanced-orange)

------------------------------------------------------------------------------------------------------------

## Data Analyst | Turning Data into Revenue-Driving Insights  


**Technical Skills:**
- **Programming:** Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- **Data Visualization:** Power BI, Excel, Matplotlib, Seaborn
- **Data Analysis:** Statistical Analysis, Data Cleaning, EDA, Predictive Modeling
- **Tools:** Jupyter Notebook, Git, SQL, Excel Advanced Formulas

------------------------------------------------------------------------------------------------------------

## 📊 Projects Portfolio

### 📈 Case Study: London Real Estate Investment Estimator

- **Client Type**: Real Estate Investment Firms & Property Arbitrage Investors in London

- **Problem**: Price ≠ Value: Traditional analysis misses location nuances and guest sentiment, causing investors to overpay for 'overpriced junk' or miss undervalued gems

- **My Approach**: Built end-to-end ML engine analyzing 96,000 listings with 150+ features; applied NLP (VADER) on 50,000+ reviews for sentiment scoring, geospatial engineering (Haversine distance), and XGBoost regression to predict fair market value

- **Result**: Achieved R² of 0.82 (MAE $28); discovered 'Bedrooms & Privacy' drive price 3x more than sentiment; properties within 5km of center command 40% premium; successfully identified undervalued arbitrage opportunities

- **Tools**: Python, Pandas, NumPy, XGBoost, Scikit-Learn, NLTK (VADER), Folium, Haversine, Streamlit

[Live App](https://london-real-estate-investment-estimator.streamlit.app/) | [GitHub](Projects/London-Real-Estate-Investment-Estimator--main)

![Map](Projects/London-Real-Estate-Investment-Estimator--main/Visuals/London_Heatmap.png)

------------------------------------------------------------------------------------------------------------


### 📈 Case Study: E-Commerce Data Analysis & Customer Segmentation

- **Client Type:** Transnational E-Commerce Retailer (B2B/B2C) with 4,200+ customers across multiple countries

- **Problem:** No unified view of customer value or behavior: marketing spend was inefficient, churn was unaddressed, and high-value segments were being overlooked  

- **My Approach:** Analyzed 540K+ transactions using Python (Pandas, RFM + Cohort analysis); engineered a two-tier dataset strategy to separate financial reporting from behavioral analysis; built interactive Power BI dashboard for executive decision-making

- **Result:** Identified 'Champions' segment (643 customers) driving ~80% of revenue; discovered 80% of daily revenue concentrates on Thursdays 10AM–3PM; revealed 3-month retention drop-off; delivered 4 actionable strategies including VIP program and targeted win-back campaigns

- **Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Power BI, Tableau, Git/GitHub  

**[Kaggle Notebook](https://www.kaggle.com/code/ahmedealtwy/e-commerce-analysis) | [GitHub](Projects/E-Commerce-Analysis) | [Executive Summary PDF](https://github.com/AhmedElatwy/E-Commerce-Analysis/blob/f05ce116202147f0e8b7037291c201c1ea2b6f4c/Excutive%20Summary.pdf)**


![E-Commerce Business Analysis Dashboard](Projects/E-Commerce-Analysis/Visual/Summary-Dashboard-2.png)

------------------------------------------------------------------------------------------------------------


### 📈 Case Study: London Bike-Sharing Demand Forecasting

- **Client Type:** "Urban Mobility Operator Managing London's Public Bike-Sharing Fleet"  

- **Problem:** "Unpredictable demand spikes and weather-driven fluctuations caused inefficient fleet redistribution, leading to empty stations during rush hour and idle bikes during off-peak times"  

- **My Approach:** "Analyzed 2+ years of historical ride data (2015-2017) combined with weather APIs; engineered temporal features (hourly/weekly patterns) and trained a Random Forest Regressor to forecast demand at station-level granularity"  

- **Result:** "Achieved R² of 0.95 in demand prediction; identified commuter-driven peaks at 8AM/5PM, temperature as the #1 demand driver, and 39% rain-induced drop with 61% user retention; enabled data-backed staffing and maintenance scheduling"  

- **Tools:** Python, Pandas, Scikit-Learn (Random Forest), Matplotlib, Seaborn, Weather APIs  

**[GitHub Repository](Projects/London-Bike-Sharing-Analysis)**


![London Bike Sharing Dashboard](Projects/London-Bike-Sharing-Analysis/Visuals/London-Bike-Dashboard.png)

------------------------------------------------------------------------------------------------------------


### [Telco Customer Churn Analysis](Projects/Telco-Customer-Churn-Analysis)
### 📈 Case Study: Telco Customer Churn Analysis

**Client Type:** Mid-size Telecommunications Provider Facing High Customer Attrition

**Problem:** Customer churn costing millions annually, with no clear visibility into *who* is leaving, *why*, or *when* to intervene

**My Approach:** Analyzed telecom customer dataset using Python (Pandas, Scikit-Learn); performed exploratory analysis to identify churn drivers, built predictive segmentation, and designed an interactive Power BI-style dashboard for retention teams

**Result:** Discovered month-to-month customers churn at 42.7% vs 2.9% for 2-year contracts; 55.5% of churn happens in Year 1; security services reduce churn risk by 65%; electronic check users are 3x more likely to leave → delivered 4 targeted retention strategies

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, Power BI (Dashboard)  

**[Kaggle Notebook](https://www.kaggle.com/code/ahmedealtwy/analyze-customer-churn-for-a-telecom-company) | [GitHub](Projects/Telco-Customer-Churn-Analysis)**

![Telco Customer Churn Analysis Dashboard](Projects/Telco-Customer-Churn-Analysis/Visual/Telco-Dashboard.png)

------------------------------------------------------------------------------------------------------------

### 📈 Case Study: Store Sales Forecasting

**Client Type:** Drugstore Retail Chain Operating 1,115 Stores

**Problem:** Inaccurate 6-week sales forecasts led to costly stockouts and overstocking, disrupting inventory operations across 1,115 stores

**My Approach:** Conducted Time Series EDA to uncover weekly seasonality (Sunday closures) and promotion impact; engineered features for seasonality and business events; identified and resolved critical data leakage by removing future 'Customers' variable; trained Random Forest Regressor for production-ready forecasting

**Result:** Quantified promotions drive ~$3,000/day median sales lift; achieved R² of 0.85 (MAE $600-800) in production-realistic conditions; model accurately predicted sales spikes and Sunday closure drops for reliable inventory planning

**Tools:** Python, Scikit-Learn, Random Forest, Pandas, Time Series Analysis, Feature Engineering, Streamlit  

**[Live Streamlit App](https://rossman-store-sales-forecasting.streamlit.app/) | [GitHub](Projects/Store-Sales-Forecasting)**

![Streamlit Live Web Interface for Real-Time Prediction.](Projects/Store-Sales-Forecasting/Visuals/Streamlit-Full.png)

------------------------------------------------------------------------------------------------------------


### 📈 Case Study: E-Commerce Revenue & Logistics Analysis (SQL)

**Client Type:** Brazilian Multi-Category E-Commerce Marketplace with 100K+ Orders

**Problem:** CMO lacked visibility into revenue drivers and high-value customers; Operations team couldn't pinpoint root causes of 29-day delivery delays in remote Amazon regions; Logistics needed network visualization to validate warehouse placement

**My Approach:** Built SQLite relational database querying 100K+ orders across 9 tables; engineered SQL + Python pipeline joining 5 relational tables to link orders to geocoordinates; calculated Haversine Distance via Vectorized NumPy; solved 'Session vs. User' identity using customer_unique_id for LTV; applied CTEs + Window Functions (LAG) for retention analysis  

**Result:** Identified Health & Beauty as top category with exponential growth ($134→$119K/month); pinpointed Northern Region bottleneck (29-day avg delivery in RR/AP/AM); generated VIP list (Top Whale: R$13.4K) for loyalty program; visualized 'Last Mile' density confirming need for São Paulo distribution hubs; flagged international shipping anomalies for data governance review  

**Tools:** SQL (SQLite), Python (Pandas, NumPy, Folium), Geospatial Analysis (Haversine), Window Functions, CTEs  

**[GitHub Repository](Projects/E-Commerce-Revenue-Logistics-Analysis-SQL)**

![Map](Projects/E-Commerce-Revenue-Logistics-Analysis-SQL/Findings/Map.png)

------------------------------------------------------------------------------------------------------------

### [Credit Card Customer Segmentation](Projects/Customer-Segmentation-Strategy)
**Tools:** Power BI, Python, Statistics, Segmentation
- Segmented a customer base to replace generic marketing with targeted, behavior-based campaigns.
- Applied K-Means Clustering and PCA on financial data, utilizing Logarithmic Transformations to handle "Whale" outliers without losing data integrity.
- Identified 4 distinct personas (e.g., "Sleeping Giants," "VIP Spenders") and drafted specific retention and activation strategies for each segment.
  
![Credit Card Customer Segmentation PCA](Projects/Customer-Segmentation-Strategy/Visuals/Customer-Segment-PCA.png)

------------------------------------------------------------------------------------------------------------

### [Automated Lithology Prediction using Well Log Data](Projects/Automated-Lithology-Prediction-using-Well-Log-Data)
**Tools:** Power BI, Python, Statistics, Petrophysics
- Built a Machine Learning pipeline to automate rock type classification (Sandstone vs. Shale) from raw well log data.
- Leveraged geophysics knowledge to perform domain-specific cleaning, choosing to drop unreliable PEF logs while preserving the "Triple Combo" signal.
- Trained a Random Forest Classifier achieving 91.7% accuracy and 95% recall on reservoir sandstones, validated via a blind-test log plot.

------------------------------------------------------------------------------------------------------------

### [Logistics Bottleneck Analysis (Supply Chain)](Projects/Logistics-Bottleneck-Analysis)
**Tools:** Power BI, Python, Statistics, Supply Chain
- Investigated the root causes of a 60% late delivery rate for an international logistics firm.
- Discovered a critical "Discount Cliff," revealing that shipments with >10% discounts were systematically deprioritized and delayed.
- Built an operational Power BI dashboard tracking warehouse performance and provided data-driven recommendations to optimize shipping priority rules.

------------------------------------------------------------------------------------------------------------

### [IBM HR Analysis](Projects/IBM-HR-Analysis)
**Tools:** Power BI, Python, Statistics
- Disproved the common belief that "lack of promotions" causes attrition.
- Identified a "Toxic Zone" where Sales Representatives working Overtime with low pay had a 40% attrition rate.
- Built a predictive model (Accuracy: 88.8%) that flags high-risk employees before they quit.

------------------------------------------------------------------------------------------------------------
    
### [Retail Strategy Analytics - Chip Category Performance](Projects/Retail-Strategy-Analytics-Chip-Category-Performance-Analysis)
**Tools:** Python, Pandas, Matplotlib, Statistical Analysis
- Analyzed chip category performance across multiple regions
- Identified key drivers of sales and customer preferences
- Provided strategic recommendations for product placement and promotions

------------------------------------------------------------------------------------------------------------

### [Social Media Emotions Analysis](Projects/Social-Media-Emotions)
**Tools:** Python, Text Analysis, Machine Learning
- Performed sentiment analysis on social media posts
- Classified emotions using machine learning algorithms
- Visualized emotional trends and patterns

------------------------------------------------------------------------------------------------------------


### [British Airways Reviews Analysis](Projects/British-Airways-Reviews-Analysis)
**Tools:** Python, Web Scraping, Sentiment Analysis
- Collected and analyzed customer reviews
- Identified key satisfaction drivers and pain points
- Provided insights for service improvement

------------------------------------------------------------------------------------------------------------


### [Stock Market Analysis (2020-2024)](Projects/Stock-Market-Analysis-2020-2024)
**Tools:** Python, Financial Analysis, Time Series
- Analyzed stock performance across multiple sectors
- Identified market trends and volatility patterns
- Developed risk assessment models

------------------------------------------------------------------------------------------------------------

### [Global Traffic Index Analysis](Projects/Traffic-Index)
**Tools:** Python, Data Visualization, Comparative Analysis
- Analyzed traffic patterns across major cities
- Identified congestion factors and peak hours
- Provided urban planning insights

------------------------------------------------------------------------------------------------------------

### [Retail Sales Analysis](Projects/retail-analysis)
**Tools:** Excel, Power BI, Business Intelligence
- Comprehensive sales performance analysis
- Inventory optimization recommendations
- Customer segmentation and targeting strategies

------------------------------------------------------------------------------------------------------------


### [International Retail Sales Analysis](Projects/International_retail_sales_analysis)
**Tools:** Power BI, Comparative Analysis, Market Research
- Cross-country sales performance comparison
- Market entry strategy recommendations
- Cultural and regional buying pattern analysis

------------------------------------------------------------------------------------------------------------


### [Supermarket Performance Analysis](Projects/SuperMarket_Analysis)
**Tools:** Excel, Data Modeling, Business Analytics
- Store performance benchmarking
- Product category optimization
- Customer loyalty program analysis

------------------------------------------------------------------------------------------------------------


### [Real Estate House Sales Analysis](Projects/HouseSales)
**Tools:** Python, Real Estate Analytics, Geographic Analysis
- Property value trend analysis
- Location-based pricing strategies
- Market demand forecasting

------------------------------------------------------------------------------------------------------------


### [IBM Data Analytics Capstone](Projects/ibm-capstone)
**Tools:** Python, End-to-End Data Analysis, Machine Learning
- Comprehensive data analysis project covering entire pipeline
- Predictive modeling and business insights
- Final capstone project for IBM certification

------------------------------------------------------------------------------------------------------------


## 🛠️ Technical Skills

| Category | Technologies |
|----------|--------------|
| **Programming** | Python, SQL |
| **Libraries** | Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn |
| **Visualization** | Power BI, Excel, Plotly |
| **Tools** | Jupyter Notebook, Git, GitHub |
| **Methodologies** | Data Cleaning, EDA, Statistical Analysis, Machine Learning |

------------------------------------------------------------------------------------------------------------


## 📫 Connect With Me

- **Email:** ahmed.abbas.elatwy@gmail.com
- **GitHub:** [https://github.com/AhmedElatwy](https://github.com/AhmedElatwy)

------------------------------------------------------------------------------------------------------------


## 📄 Certifications

- IBM Professional Data Analyst
- Google Advanced Data Analysis
- Bachelor of Science


------------------------------------------------------------------------------------------------------------



*This portfolio is continuously updated with new projects and improvements.*
