import pandas as pd
words_series = pd.Series(['apple', 'banana', 'cherry', 'date'])
word_lengths = words_series.apply(lambda x: len(x))
result_df = pd.DataFrame({'Word': words_series, 'Length': word_lengths})
print(result_df)
