import pandas as pd
data = pd.Series([[1, 2, 3], [4, 5], [6, 7, 8]])
result = data.explode()
print(result)
