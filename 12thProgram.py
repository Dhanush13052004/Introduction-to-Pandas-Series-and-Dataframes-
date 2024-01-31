import pandas as pd
import numpy as np
data = {'A': [1, 2, np.inf, 4],
        'B': [5, np.inf, 7, 8]}
df = pd.DataFrame(data)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df_cleaned = df.dropna()
print("DataFrame after removing infinite values:")
print(df_cleaned)
