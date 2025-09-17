import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ---------------- Sample Data ----------------

# For numeric plots (line, scatter, histogram)
data_num = pd.DataFrame({
    'X': range(10),
    'Y': [5, 9, 8, 6, 7, 4, 2, 6, 7, 8]
})

# For categorical plots (bar, box)
data_cat = pd.DataFrame({
    'Category': ['A','B','C','D','A','B','C','D','A','B'],
    'Values': [23,45,12,36,25,40,15,38,30,42]
})

# ---------------- Matplotlib Plots ----------------

# Line plot
plt.figure(figsize=(6,4))
plt.plot(data_num['X'], data_num['Y'], marker='o', color='blue')
plt.title("Matplotlib Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar chart
plt.figure(figsize=(6,4))
plt.bar(data_cat['Category'], data_cat['Values'], color='skyblue')
plt.title("Matplotlib Bar Chart")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()

# Histogram
plt.figure(figsize=(6,4))
plt.hist(data_num['Y'], bins=5, color='lightgreen')
plt.title("Matplotlib Histogram")
plt.xlabel("Y Values")
plt.ylabel("Frequency")
plt.show()

# ---------------- Seaborn Plots ----------------

# Scatter plot
plt.figure(figsize=(6,4))
sns.scatterplot(x='X', y='Y', data=data_num, color='red', s=100)
plt.title("Seaborn Scatter Plot")
plt.show()

# Box plot
plt.figure(figsize=(6,4))
sns.boxplot(x='Category', y='Values', data=data_cat)
plt.title("Seaborn Box Plot")
plt.show()

# Heatmap (correlation of numeric data)
corr = data_num.corr()
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Seaborn Heatmap")
plt.show()
