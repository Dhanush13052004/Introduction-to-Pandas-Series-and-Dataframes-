import pandas as pd
data = pd.Series([10, 15, 20, 25, 30, 35, 40, 45, 50])
positions = data.index[data % 5 == 0].tolist()
print("Positions of numbers that are multiples of 5:")
print(positions)
