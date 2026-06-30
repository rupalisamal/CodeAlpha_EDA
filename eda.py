import pandas as pd
import matplotlib .pyplot as plt
import seaborn as sns

df = pd.read_csv("tested.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print("Missing % in each column:")
print((df.isnull().sum() / len(df)) * 100)

sns.countplot(x='Survived',data=df)
plt.title("Survival Count")
plt.show()
#Question 1: Did gender affect survival rate?
print("survival Rate by Gender:")
print(df.groupby('Sex')['Survived'].mean())

#Question 2: Did passenger class affect survival rate?
print("Survival Rate by Passenger Class:")
print(df.groupby('Pclass')['Survived'].mean())

plt.figure(figsize=(8,5))
sns.histplot(df['Age'],bins=20,kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

#Question 3: Did age affect survival rate?
plt.figure(figsize=(8,5))
sns.boxplot(x="Survived", y= 'Age', data = df)
plt.title("Age vs Survival")
plt.show()


plt .figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),annot=True,
cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()            

#Observations:
#1. Female survival rate was significantly higher than male survival rate.
#2. 1st class passenger had the highest survival rate (46.7%) compared to 2nd/3rd class (~32-33%)
#3. Age did not show a clear strong affect on survival, unlike gender/class
#4. The cabin column had the highest number of missing values
#5. Fare and survival had a positive correlation (0.19) while Pclass and fare were negatively correlated (~0.58)
#  which means passenger who paid higher fare(mostly 1st class ) had better chance of survival.