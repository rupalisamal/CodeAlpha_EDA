# 📊 CodeAlpha - Exploratory Data Analysis (EDA)

## 🎯 Internship Task
This project is submitted as part of the **Data Analytics Internship at CodeAlpha**.  
**Task 2: Exploratory Data Analysis (EDA)**

## 📌 Objective
To perform an in-depth exploratory data analysis on the Titanic dataset in order to:
- Understand the structure of the data
- Identify trends, patterns, and anomalies
- Test hypotheses around survival using statistics and visualization
- Detect data quality issues such as missing values

## 🗂️ Dataset
The dataset used is the **Titanic Dataset** (`tested.csv`), which contains information about passengers aboard the Titanic, including their age, gender, passenger class, fare, and survival status.

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Python | Core programming language for analysis |
| Pandas | Data loading, cleaning, and exploration |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualizations (heatmap, boxplot, histplot) |
| VS Code | Development environment |
| GitHub | Version control and project documentation |

## 🔍 Analysis Performed

### 1. Data Structure & Quality Check
- Inspected dataset shape, column types, and summary statistics using `.head()`, `.info()`, and `.describe()`
- Calculated missing values and their percentage across all columns

### 2. Key Questions Explored
- **Question 1:** Did gender affect survival rate?
- **Question 2:** Did passenger class affect survival rate?
- **Question 3:** Did age affect survival rate?

### 3. Visualizations
- Survival Count (Bar Plot)
- Age Distribution (Histogram with KDE)
- Age vs Survival (Box Plot)
- Correlation Heatmap

## 📈 Key Observations
1. Female survival rate was significantly higher than male survival rate.
2. 1st class passengers had the highest survival rate (46.7%) compared to 2nd/3rd class (~32-33%).
3. Age did not show a clear strong effect on survival, unlike gender/class.
4. The Cabin column had the highest number of missing values.
5. Fare and Survival had a positive correlation (0.19), while Pclass and Fare were negatively correlated (-0.58) — meaning passengers who paid higher fares (mostly 1st class) had better chances of survival.

## ⚠️ Important Note on Dataset
Upon deeper analysis, this dataset (`tested.csv`) was found to follow a gender-based 
survival pattern (all female passengers marked as survived, all male passengers marked 
as not survived), rather than representing real mixed historical outcomes. This explains 
the strong correlation between gender and survival in this analysis. The other patterns 
(class, fare) are influenced by this underlying gender split.


## ✅ Conclusion
This EDA reveals that **gender, passenger class, and fare** were the strongest indicators of survival on the Titanic, while age alone did not show a significant impact. This highlights how socio-economic factors influenced survival outcomes during the disaster.

## 📚 What I Learned
- Data cleaning and missing value analysis are essential first steps before drawing any conclusions
- Visualizations like boxplots help compare distributions across categories more effectively than raw numbers
- Correlation heatmaps are useful for spotting relationships between multiple variables at once
- Framing analysis around clear questions makes the entire EDA process more structured and purposeful

## 🚀 Future Improvements
- Apply machine learning models to predict survival based on the explored features
- Handle missing Age and Cabin values using imputation techniques instead of just identifying them
- Build an interactive dashboard for the visualizations

## ▶️ How to Run
1. Clone this repository
2. Install required libraries:
   ```
   pip install pandas matplotlib seaborn
   ```
3. Run the script:
   ```
   python eda.py
   ```

---
**Internship:** CodeAlpha Data Analytics Internship  
**Task:** Exploratory Data Analysis (EDA)
