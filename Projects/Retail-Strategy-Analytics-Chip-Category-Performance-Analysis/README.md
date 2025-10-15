# 🛒 Retail Strategy & Analytics: Chip Category Performance Analysis

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Statistical Analysis](https://img.shields.io/badge/Statistical_Analysis-8A2BE2?style=for-the-badge)](https://)

## 📊 Project Overview

Comprehensive retail analytics project conducted for Quantium to analyze customer purchasing behavior in the chips category and evaluate the impact of new trial store layouts. This data-driven analysis provided strategic recommendations for optimizing sales and customer engagement.

### 🎯 Business Objectives
- Analyze customer purchasing behavior for chips category
- Identify key customer segments and sales drivers  
- Evaluate impact of trial store layouts vs control stores
- Provide data-driven recommendations for national rollout

## 📈 Key Insights & Findings

### Customer Segmentation
- **Top Segments:** Retirees (20.38%), Older Singles/Couples (20.11%), Young Singles/Couples (19.88%)
- **Membership Distribution:** Mainstream (40.26%), Budget (33.69%), Premium (26.05%)
- **Spending Patterns:** New Families pay highest average price ($3.91), indicating premium preferences

### Sales Performance
- **Top Product:** Kettle Mozzarella Basil & Pesto 175g ($33,043.50 total sales)
- **Popular Pack Size:** 175g (25.1% of total sales)
- **Sales Trends:** Significant fluctuations with peaks in January 2019 (6,900 units)

### Trial Store Impact
| Trial Store | Control Store | Max Sales Increase | Statistical Significance |
|-------------|---------------|-------------------|--------------------------|
| Store 77    | Store 233     | 41.91% (Apr 2019) | ✅ All months significant |
| Store 88    | Store 237     | 20.47% (Mar 2019) | ✅ All months significant |
| Store 86    | Store 155     | 21.14% (Mar 2019) | ⚠️ Only March significant |

## 🛠️ Methodology

### Data Processing
- **Dataset:** 264,836 transactions, 72,637 customers
- **Cleaning:** Removed duplicates, handled outliers, validated data types
- **Preprocessing:** DateTime conversion, quantity validation, customer segmentation

### Analytical Techniques
- **Customer Segmentation:** Lifestage and membership analysis
- **RFM Analysis:** Customer value segmentation
- **Statistical Testing:** T-tests for trial impact validation
- **Control Store Matching:** Correlation analysis (0.87-0.97) and SMD (0.00-0.02)
