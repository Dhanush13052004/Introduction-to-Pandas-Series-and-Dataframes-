import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
index_labels = ['Person1', 'Person2', 'Person3']
df = pd.DataFrame(data, index=index_labels)
print(df)
