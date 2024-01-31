import pandas as pd
data = pd.Series([10, 20, 30, 40, 50, 60])
condition = data > 30
subset = data[condition]
print("Original Series:")
print(data)
print("\nSubset based on condition:")
print(subset)
