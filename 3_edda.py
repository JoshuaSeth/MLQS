import pandas as pd
import numpy.fft as fft
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import math

df = pd.read_csv('proc_data/2_filled.csv')


# Comment in our out whether to plot with or without resmapling
df['date'] = pd.to_datetime(df['time'])
df=df.set_index('date')
df = df.resample('100ms').mean()

print(df)


df = df.astype(np.float16)




# Fill empty spaces
df = df.interpolate()

df= df.drop('time', axis=1)

# sns.lineplot(data=normalized_df.drop('time', axis=1))
figspercol = math.ceil(len(df.columns)/4)
fig, ax = plt.subplots(ncols=4, nrows=figspercol)

idx=0
for row in ax:
    rowidx=0
    for col in row:
        try:
            if rowidx < figspercol-1:
                col.set_xticks([])
                col.set_xticks([], minor=True)
            col.plot(df.iloc[:, idx])
            col.set_title(df.columns[idx], fontdict = {'fontsize' : 8}, pad=0)
            idx+=1
            rowidx+=1
        except Exception as e: pass

plt.show()