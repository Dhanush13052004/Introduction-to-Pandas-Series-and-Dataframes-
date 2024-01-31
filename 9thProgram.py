import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)
def append_and_delete_row(dataframe, new_row_values):
    dataframe = dataframe.append(new_row_values, ignore_index=True)
    print("DataFrame after appending a new row:")
    print(dataframe)
    dataframe = dataframe.drop(dataframe.index[-1])
    print("\nDataFrame after deleting the new row:")
    print(dataframe)
    return dataframe
new_row_values = {'Name': 'David', 'Age': 28, 'City': 'Chicago'}
original_dataframe = append_and_delete_row(df, new_row_values)
print("\nOriginal DataFrame after appending and deleting:")
print(original_dataframe)
