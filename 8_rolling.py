import pandas as pd

df = pd.read_csv('proc_data/7_clusters.csv')

print(df)

df['date'] = pd.to_datetime(df['time'])

df= df.drop('time', axis=1)

df=df.set_index('date')

df = df.resample('10S').mean()

df = df.drop(['light', 'intense'], axis=1)

df.to_csv('proc_data/8_resampled.csv')