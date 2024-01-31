import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'Score': [85, 92, 78, 90, 88]}
df = pd.DataFrame(data)
sorted_df = df.sort_values(by=['Name', 'Score'], ascending=[False, True])
print("Sorted DataFrame:")
print(sorted_df)
