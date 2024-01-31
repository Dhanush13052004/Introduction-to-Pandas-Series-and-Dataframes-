import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Qualify': ['yes', 'no', 'yes']}
df = pd.DataFrame(data)
df['Qualify'] = df['Qualify'].replace({'yes': True, 'no': False})
print("DataFrame after replacing values:")
print(df)
