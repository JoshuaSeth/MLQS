import pandas as pd

df = pd.read_csv('proc_data/4_frequencies.csv')

# Now we only take a certain percentage of overlap in the windows, otherwise our training examples will be too much alike.
milliseconds_per_instance=200


fs = float(1000)/milliseconds_per_instance
ws = int(float(10000)/milliseconds_per_instance)

# # The percentage of overlap we allow
window_overlap = 0.95
skip_points = int((1-window_overlap) * ws)
print('skipping', skip_points)
df = df.iloc[::skip_points,:]

df.to_csv('proc_data/5_overlap.csv', index=False)