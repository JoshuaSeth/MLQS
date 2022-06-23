from frequencies import FourierTransformation
import copy
import pandas as pd

df = pd.read_csv('proc_data/2_filled.csv')

# First resample it else it wouldn't be truly temporal
df['date'] = pd.to_datetime(df['time'])
df=df.set_index('date')
df = df.resample('200ms').mean()
df = df.set_index('time')

# We probably still have nans after resampling # CHOICE HERE: either resample coarse and have less NANs or resample fine and interpolate NANs
# Choose for finegrained since it allows for detecting finer frequencies and probably interpolation between 2 accelerometer measurements is fairly accurate over a ms/s scale. Also later we will resample to minute
print(df[df.isna().any(axis=1)].shape, df.shape)
df=df.interpolate()
df = df.dropna()
print(df[df.isna().any(axis=1)].shape)

print(df.shape)
milliseconds_per_instance=200

FreqAbs = FourierTransformation()

fs = float(1000)/milliseconds_per_instance
ws = int(float(10000)/milliseconds_per_instance)
selected_predictor_cols = [c for c in df.columns if ((not 'annotation' in c) and (not 'time' in c) and (not 'date' in c)and (not 'target' in c))]



df = FreqAbs.abstract_frequency(copy.deepcopy(df), selected_predictor_cols, int(float(10000)/milliseconds_per_instance), fs)

print('shape', df.shape)

df['time'] = df.index
df.to_csv('proc_data/4_frequencies.csv', index=False)