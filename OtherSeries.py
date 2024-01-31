import pandas as pd
data = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5])
most_frequent_value = data.mode().iloc[0]
data = data.apply(lambda x: most_frequent_value if x == most_frequent_value else 'Other')
print(data)
