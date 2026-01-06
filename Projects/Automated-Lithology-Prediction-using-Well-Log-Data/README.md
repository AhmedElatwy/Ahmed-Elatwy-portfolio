# Automated Lithology Prediction using Well Log Data

### The Business Problem:
In oil & gas exploration, determining rock lithology (sandstone vs. shale) is critical for identifying potential reservoirs. However, manual interpretation of wireline logs across hundreds of legacy wells is time-consuming, expensive, and subject to human bias. The exploration team needed an automated solution to classify rock types rapidly using raw log data.

### My Role & Approach:
I acted as a Petrophysical Data Analyst, building a Machine Learning pipeline to classify lithology from North Sea well data (Force 2020 Dataset).

## 	Data Cleaning Strategy (Domain-Specific):
o	Handled massive missing data in the PEF (Photoelectric Factor) log. Instead of using standard imputation (which would fabricate geological data), I utilized domain knowledge to drop the unreliable feature while preserving critical reservoir rows.
o	Performed "Gap Analysis" to differentiate between small measurement glitches (interpolated) and large unlogged sections (dropped).
## 	Exploratory Data Analysis (EDA):
o	Created industry-standard Triple Combo Log Plots using Matplotlib to visualize Gamma Ray and Density tracks.
o	Developed NPHI-RHOB Crossplots to validate the physical "Sand vs. Shale" trends before modeling.
•	Machine Learning Modeling:
o	Trained a Random Forest Classifier to handle the non-linear nature of geological data.
o	Used a feature set of Gamma Ray (GR), Density (RHOB), and Neutron Porosity (NPHI) to predict lithology classes.
## The Results
•	91.7% Classification Accuracy on the test set.

•	95% Recall on Sandstone (Reservoir Rock): The model successfully identified the "Pay Zone," minimizing the risk of missing economic opportunities.

•	Visual Validation: Generated a "Blind Test" log plot comparing the model's predictions against the actual core-calibrated lithology, showing near-perfect alignment in the reservoir section (2250m–2380m).

![lithology Actual vs Prediction](https://github.com/AhmedElatwy/Automated-Lithology-Prediction-using-Well-Log-Data/blob/32016e64e9ca50aaa2d27755424f93724aaf8b52/Visuals/lithology%20Actual%20vs%20Prediction%202.png)
## Tools Used
•	Python: Pandas, NumPy, Scikit-Learn.

•	Visualization: Matplotlib (Custom Log Tracks), Seaborn.

•	Concepts: Supervised Learning, Petrophysics, Feature Engineering.

