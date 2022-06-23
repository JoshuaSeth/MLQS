import pandas as pd
import numpy as np

df = pd.read_csv('proc_data/5_overlap.csv')

cors = []

for col in df.columns:
    cor =np.abs(df[col].corr(df['target']))
    cors.append([cor, col])

cordf = pd.DataFrame(cors)
cordf=cordf.sort_values(0)

cordf.to_csv('misc/correlations.csv')