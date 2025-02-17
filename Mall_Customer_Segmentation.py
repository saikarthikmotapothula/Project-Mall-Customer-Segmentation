#Data Collection and Cleaning
import pandas as pd
# Load the dataset
file_path = 'Mall_Customers.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset and column names
print(data.head(10))
print(data.columns)

# Renaming columns for better readability if needed
data.columns = ["CustomerID", "Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"]

# Check for missing values
count = data.isnull().sum()
print(count)

# Fill missing values for 'Age' with the mean
mean_age = data['Age'].mean()
data["Age"].fillna(mean_age, inplace=True)

# Drop rows with any remaining missing values (if any)
data.dropna(inplace=True)

# Check again for missing values to confirm
count = data.isnull().sum()
print(count)

# Encode 'Gender' column
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Save the cleaned dataset
data.to_csv('cleaned_mall_customers.csv', index=False)
print(data.head(10))

#Exploratory Data Analysis (EDA)

import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
data = pd.read_csv('cleaned_mall_customers.csv')

# Calculate descriptive statistics
print(data.describe())

# Visualize Age distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.show()

# Visualize Annual Income distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Annual Income (k$)'], bins=30, kde=True)
plt.title('Annual Income Distribution')
plt.show()

# Visualize Spending Score distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Spending Score (1-100)'], bins=30, kde=True)
plt.title('Spending Score Distribution')
plt.show()

# Scatter plot of Annual Income vs. Spending Score, colored by Gender
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender')
plt.title('Income vs Spending Score')
plt.show()

#Customer Segmentation
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the cleaned dataset
data = pd.read_csv('cleaned_mall_customers.csv')

# Select features for clustering
features = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(scaled_features)

# Plot customer segments
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette='viridis')
plt.title('Customer Segments')
plt.show()

# Save the clustering results
data.to_csv('clustered_mall_customers.csv', index=False)
