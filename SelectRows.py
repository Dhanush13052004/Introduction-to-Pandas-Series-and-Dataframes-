import pandas as pd
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'attempts': [1, 3, 2, 4],
        'score': [80, 92, 75, 88]}
df = pd.DataFrame(data)
selected_rows = df[df['attempts'] > 2]
print("Rows where the number of attempts is greater than 2:")
print(selected_rows)
