# **Credit Card Customer Segmentation Project**

## 📋 Project Overview
This project applies unsupervised machine learning to segment credit card holders into distinct behavioral groups for targeted marketing and risk management strategies. Using K-Means clustering and PCA, we identified 4 customer personas from 8,894 credit card holders.

## 📊 Dataset Information
- **Source**: Kaggle - Credit Card Dataset for Clustering
- **Records**: 8,950 initial customers
- **Features**: 17 behavioral and financial attributes
- **Target**: Unsupervised segmentation

## 🛠️ Data Cleaning & Preprocessing
### **Handled Issues:**
- **Missing Values**: 
  - MINIMUM_PAYMENTS (3.5% missing) → Predictive Imputation using IterativeImputer
  - CREDIT_LIMIT (1 null) → Median imputation
- **Data Integrity**:
  - Fixed negative MINIMUM_PAYMENTS values
  - Capped CASH_ADVANCE_FREQUENCY to maximum of 1.0
- **Outlier Treatment**:
  - Applied log transformation to financial columns to handle extreme outliers

## 🔧 Methodology

### **1. Feature Engineering**
```python
# Key preprocessing steps:
- StandardScaler for feature normalization
- Log transformation for skewed financial data
- PCA for dimensionality reduction (2 components for visualization)
```

### **2. Clustering Algorithm**
- **Algorithm**: K-Means Clustering
- **Optimal Clusters**: 4 (determined by Elbow Method & Silhouette Score)
- **Validation**: Silhouette Score analysis for cluster quality

### **3. Visualization**
- PCA for 2D cluster visualization
- Feature importance analysis for segment interpretation

## 👥 Customer Segments Identified

### **1. 🟦 Average Joes (3,088 customers - 36%)**
```
Financial Snapshot:
• Balance: $1,860      • Purchases: $837
• Credit Limit: $4,218 • Full Payment: 6%

Behavior: Moderate usage, carries balance, rarely pays in full
Strategy: Increase full payments via auto-pay incentives
```

### **2. 🟩 Responsible Regulars (2,190 customers - 26%)**
```
Financial Snapshot:
• Balance: $72         • Purchases: $493
• Credit Limit: $3,382 • Full Payment: 35%

Behavior: Low balances, good payment habits, steady usage
Strategy: Increase spending with targeted offers
```

### **3. 🟨 Sleeping Giants (2,129 customers - 25%)**
```
Financial Snapshot:
• Balance: $2,328      • Purchases: $10
• Credit Limit: $4,165 • Full Payment: 3%

Behavior: High limits, minimal usage, untapped potential
Strategy: Activate spending with welcome-back campaigns
```

### **4. 🟥 VIP Spenders (1,487 customers - 18%)**
```
Financial Snapshot:
• Balance: $2,086      • Purchases: $3,550
• Credit Limit: $7,045 • Full Payment: 24%

Behavior: High spending, frequent usage, premium customers
Strategy: Retain with VIP programs and exclusive offers
```
![Customer Segment PCA](https://github.com/AhmedElatwy/Customer-Segmentation-Strategy/blob/16a6b8daa201c4f0cb9d8948562215c60792f1e4/Visuals/Customer%20Segment%20PCA.png)
## 📈 Business Impact

### **Revenue Insights:**
```
Total Monthly Revenue Estimate: ~$487,000
Segment Contribution:
• VIP Spenders: Highest per-customer revenue
• Average Joes: Largest revenue base
• Sleeping Giants: Highest untapped potential
• Responsible Regulars: Lowest risk
```

### **Strategic Recommendations:**
1. **Activation Campaigns** for Sleeping Giants (25% of customers)
2. **Retention Programs** for VIP Spenders (highest value customers)
3. **Payment Optimization** for Average Joes (largest segment)
4. **Growth Initiatives** for Responsible Regulars (low-risk expansion)


## 👥 Contributors
Ahmed Elatwy - Data Analysis & Clustering

**Project Status**: ✅ COMPLETE  
**Last Updated**: [01/01/2026]  
