import pandas as pd
year_month_series = pd.Series(['2022-01', '2022-02', '2022-03'])
day_to_add = 15
result_dates = pd.to_datetime(year_month_series) + pd.to_timedelta(day_to_add - 1, unit='D')
result_df = pd.DataFrame({'Year-Month': year_month_series, 'Result Date': result_dates})
print(result_df)
