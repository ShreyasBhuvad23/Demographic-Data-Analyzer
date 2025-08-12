import pandas as pd

# Load demographic data from CSV
data = pd.read_csv('demographic_data.csv')

# Show the first few rows
print("Preview of data:")
print(data.head())

# Summary statistics
print("\nSummary statistics:")
print(data.describe())

# Count unique countries
if 'country' in data.columns:
    print("\nNumber of unique countries:", data['country'].nunique())

# Age distribution
if 'age' in data.columns:
    print("\nAge distribution:")
    print(data['age'].value_counts().sort_index())

# Gender breakdown
if 'gender' in data.columns:
    print("\nGender breakdown:")
    print(data['gender'].value_counts())