import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def summary_statistics(df):
    stats = {}
    stats['mean_age'] = df['age'].mean()
    stats['gender_counts'] = df['gender'].value_counts().to_dict()
    stats['education_counts'] = df['education'].value_counts().to_dict()
    return stats

def plot_gender_distribution(df):
    df['gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Gender Distribution')
    plt.ylabel('')
    plt.show()

def plot_age_histogram(df):
    df['age'].plot(kind='hist', bins=20, color='skyblue')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.show()

if __name__ == "__main__":
    # Example usage
    data_file = 'demographic_data.csv'  # replace with your actual file
    df = load_data(data_file)
    stats = summary_statistics(df)
    print("Summary Statistics:", stats)
    plot_gender_distribution(df)
    plot_age_histogram(df)
