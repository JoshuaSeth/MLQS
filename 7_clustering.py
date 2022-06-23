import pandas as pd
from cluster import NonHierarchicalClustering
from tqdm import tqdm
import util as util
from vizdata import VisualizeDataset

# Strongest correlations
# 44,0.3967007406306185,gravity_y
# 1065,0.40243456408511175,magnetometer_x_freq_0.0_Hz_ws_50
# 1297,0.42449287999941315,gravity_z_freq_0.0_Hz_ws_50
# 45,0.4280417724602044,gravity_x
# 32,0.44406383574080616,orientation_pitch
# 1355,0.44769024589820366,gravity_x_freq_0.0_Hz_ws_50
# 1326,0.4552940930925113,gravity_y_freq_0.0_Hz_ws_50
# 1123,0.46490276518911827,accelerometer_y_freq_0.0_Hz_ws_50
# 978,0.498117256966559,orientation_pitch_freq_0.0_Hz_ws_50


df = pd.read_csv('proc_data/5_overlap.csv')

for col in tqdm(df.columns):
    if df[col].isna().sum() > 200:
        tqdm.write(col)
        df.drop(col, axis=1)

df=df.dropna()


# Create temp column for plotting
df['intense'] = (df['target']>=9).astype(float)
df['light'] = (df['target']<9).astype(float)

print(df.shape)
df=df.dropna()
print(df.shape)

DataViz = VisualizeDataset(__file__)

first_cols = ['orientation_pitch_freq_0.0_Hz_ws_50','accelerometer_y_freq_0.0_Hz_ws_50','orientation_pitch']
second_cols = ['gravity_y_freq_0.0_Hz_ws_50', 'gravity_x_freq_0.0_Hz_ws_50', 'gravity_z_freq_0.0_Hz_ws_50']
third_cols = ['gravity_x', 'gravity_y', 'magnetometer_x_freq_0.0_Hz_ws_50']
alls_cols = [first_cols, second_cols, third_cols]

# And we select the outcome dataset of the knn clustering....
clusteringNH = NonHierarchicalClustering()
k=4
cols = df.drop(['target'],axis=1).columns

for idx, colset in enumerate(alls_cols):
    df = clusteringNH.k_means_over_instances(df, colset ,k, 'default', 50, 50, idx)
    # DataViz.plot_clusters_3d(df, colset, 'cluster', ['intense', 'light'])
    # DataViz.plot_silhouette(df, 'cluster', 'silhouette')
    # util.print_latex_statistics_clusters(df, 'cluster', cols, 'label')
    del df['silhouette']

df.to_csv('proc_data/7_clusters.csv', index=False)