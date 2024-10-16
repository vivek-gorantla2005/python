import pandas as pd
import numpy as np
# Example 1: Creating DataFrame from a simple list
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data, columns=['Numbers'])
print("DataFrame from List:")
print(df)

# Example 2: Creating DataFrame from a list of lists
data_2d = [[1, 'Alice', 25],
            [2, 'Bob', 30],
            [3, 'Charlie', 35]]
df_2d = pd.DataFrame(data_2d, columns=['ID', 'Name', 'Age'])
print("\nDataFrame from List of Lists:")
print(df_2d)


# Create a dictionary
data = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame from Dictionary:")
print(df)



#series
# Example 1: Creating a Series from a list
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)
print("Series from List:")
print(series_from_list)

# Example 2: Creating a Series from a NumPy array
data_array = np.array([100, 200, 300, 400, 500])
series_from_array = pd.Series(data_array)
print("\nSeries from NumPy Array:")
print(series_from_array)

# Example 3: Creating a Series with both a list and an array
data_combined = [1, 2, 3, 4, 5]
index_labels = np.array(['a', 'b', 'c', 'd', 'e'])
combined_series = pd.Series(data_combined, index=index_labels)
print("\nCombined Series from List with NumPy Array as Index:")
print(combined_series)
