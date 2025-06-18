# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Step 2: Load CSV file
df = pd.read_csv("Uber Request Data.csv")

# Step 3: Preview the data
print("First 5 rows:")
print(df.head())

# Step 4: Dataset Info
print("\nDataset Info:")
print(df.info())

# Check for duplicate rows
duplicate_rows = df.duplicated()

# Total number of duplicate rows
print("Total duplicate rows:", duplicate_rows.sum())

# Step 5: Missing Values Check
print("\nMissing values:")
print(df.isnull().sum())

# Drop duplicate rows
df = df.drop_duplicates()
print("\nShape after removing duplicates:", df.shape)

# Convert timestamps to datetime
df['Request timestamp'] = pd.to_datetime(df['Request timestamp'], dayfirst=True, errors='coerce')
df['Drop timestamp'] = pd.to_datetime(df['Drop timestamp'], dayfirst=True, errors='coerce')

# Check parsing results
print("Missing request timestamps:", df['Request timestamp'].isna().sum())
print("Missing drop timestamps:", df['Drop timestamp'].isna().sum())
df = df[df['Request timestamp'].notna()]

# Extract hour and day
df['Request hour'] = df['Request timestamp'].dt.hour
df['Request day'] = df['Request timestamp'].dt.date

# Create time slot column
def get_time_slot(hour):
    if pd.isna(hour): return np.nan
    if 0 <= hour < 5:
        return "Late Night"
    elif 5 <= hour < 10:
        return "Morning"
    elif 10 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

df['Time slot'] = df['Request hour'].apply(get_time_slot)

print("\nSample after cleaning:")
print(df.head())

# Univariate Analysis (Visualizing One Variable at a Time)
# 1. Request Status Distribution
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Status', order=df['Status'].value_counts().index, palette='Set2')
plt.title("Overall Trip Status Distribution")
plt.xlabel("Status")
plt.ylabel("Number of Requests")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# 2. Pickup Point Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Pickup point', palette='Set1')
plt.title("Pickup Point Distribution")
plt.xlabel("Pickup Point")
plt.ylabel("Count")
plt.show()

# 3. Requests by Time Slot
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Time slot', order=['Late Night', 'Morning', 'Afternoon', 'Evening', 'Night'], palette='coolwarm')
plt.title("Requests by Time Slot")
plt.xlabel("Time Slot")
plt.ylabel("Number of Requests")
plt.tight_layout()
plt.show()

# Bivariate Analysis
# 1. Status vs Time Slot
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Time slot', hue='Status', order=['Late Night', 'Morning', 'Afternoon', 'Evening', 'Night'], palette='pastel')
plt.title("Trip Status by Time Slot")
plt.xlabel("Time Slot")
plt.ylabel("Number of Requests")
plt.legend(title="Status")
plt.tight_layout()
plt.show()

# 2. Status vs Pickup Point
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Pickup point', hue='Status', palette='coolwarm')
plt.title("Trip Status by Pickup Point")
plt.xlabel("Pickup Point")
plt.ylabel("Number of Requests")
plt.legend(title="Status")
plt.tight_layout()
plt.show()

# 3. Heatmap: Hour vs Status
pivot = df.pivot_table(index='Request hour', columns='Status', values='Request id', aggfunc='count')
plt.figure(figsize=(12, 6))
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlGnBu')
plt.title("Request Status by Hour of the Day")
plt.ylabel("Hour")
plt.xlabel("Status")
plt.show()

# Export cleaned data to Excel for dashboarding
df.to_excel("Uber_Cleaned_Data.xlsx", index=False)
