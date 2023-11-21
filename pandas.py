import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Ella'],
    'Age': [25, 30, 35, 40, 27],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston']
}

df = pd.DataFrame(data)

# Displaying the DataFrame
print("Original DataFrame:")
print(df)
print()

# Basic DataFrame operations
print("Basic DataFrame operations:")
# Accessing columns
print("Columns in DataFrame:", df.columns)
# Accessing specific column
print("Age Column:")
print(df['Age'])
# Accessing a specific row
print("Row 2:")
print(df.iloc[1])
print()

# Filtering the DataFrame
print("Filtering based on condition (Age > 30):")
filtered_df = df[df['Age'] > 30]
print(filtered_df)
print()

# Sorting the DataFrame
print("Sorting DataFrame by Age in descending order:")
sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)
print()

# Adding a new column
df['Gender'] = ['Female', 'Male', 'Male', 'Male', 'Female']
print("DataFrame with a new 'Gender' column:")
print(df)
print()

# Grouping and aggregating data
grouped = df.groupby('Gender').mean()
print("Grouped by Gender and calculated mean age:")
print(grouped)
print()

# Saving DataFrame to a CSV file
df.to_csv('output.csv', index=False)
print("DataFrame saved to 'output.csv'")
