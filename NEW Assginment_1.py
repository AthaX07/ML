import pandas as pd
import statistics as s

df = pd.read_csv("C:/Users/Lenovo/Downloads/heart.csv")

shape = df.shape
print("Shape of dataset is:", shape)

print("Data Type for Each Column:\n", df.dtypes)

missing_values = df.isnull().sum().sort_values(ascending=False)
print("Missing Values in Each Column:\n", missing_values)

missing_percentage = (df.isnull().sum().sort_values(ascending=False) / len(df)) * 100
print("Percentage of Missing Values in Each Column:\n", missing_percentage)

zero_counts = (df == 0).sum().sort_values(ascending=False)
print("Zero Counts in Each Column:\n", zero_counts)

average_age = s.mean(df['age'])
print("Average age of the patients:", average_age)
