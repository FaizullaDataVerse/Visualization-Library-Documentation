# ---------------------------------------------------------
# Delhi AQI In-Depth Analysis: ShadowFox Internship Project
# ---------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Research Questions
"""
- What are the concentration trends of major pollutants (PM2.5, PM10, CO, NO2, SO2, O3, NH3) in Delhi?
- How do these pollutants vary seasonally?
- What is the interplay between geography, meteorology, and Delhi's high AQI values?
"""

# 2. Data Loading & Preprocessing
df = pd.read_csv(r"C:\Users\princ\Downloads\delhiaqi.csv")
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['hour'] = df['date'].dt.hour

# 3. Basic Diagnostics
print("==== Dataset Shape ====")
print(df.shape)
print("\n==== Missing Values ====")
print(df.isnull().sum())
print("\n==== Descriptive Statistics ====")
print(df.describe().T)

# 4. Monthly & Hourly Aggregations
monthly_means = df.groupby('month')[['pm2_5','pm10','co','no2','so2','o3','nh3']].mean()
hourly_means = df.groupby('hour')[['pm2_5','pm10','co','no2','so2','o3','nh3']].mean()

# 5. Correlation Matrix
plt.figure(figsize=(8,6))
sns.heatmap(df[['pm2_5','pm10','co','no','no2','so2','o3','nh3']].corr(), annot=True, cmap='vlag')
plt.title('Correlation between Pollutants in Delhi')
plt.show()

# 6. Monthly Trends Visualization
plt.figure(figsize=(8,6))
for p in ['pm2_5','pm10','co','no2','so2','o3','nh3']:
    plt.plot(monthly_means.index, monthly_means[p], marker='o', label=p.upper())
plt.xlabel('Month')
plt.ylabel('Average Concentration')
plt.title('Monthly Averages of Key Air Pollutants in Delhi')
plt.legend()
plt.grid('darkgrid')
plt.tight_layout()
plt.show()

# 7. Hourly Patterns Visualization
plt.figure(figsize=(8,6))
for p in ['pm2_5','pm10','co','no2']:
    plt.plot(hourly_means.index, hourly_means[p], marker='o', label=p.upper())
plt.xlabel('Hour of Day')
plt.ylabel('Average Concentration')
plt.title('Diurnal Patterns of Main Pollutants')
plt.legend()
plt.grid('darkgrid')
plt.tight_layout()
plt.show()
