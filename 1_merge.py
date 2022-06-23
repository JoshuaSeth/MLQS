import pandas as pd
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
from copy import deepcopy
# Get filenames
datapath = 'raw'
onlyfiles = [f for f in listdir(datapath) if isfile(join(datapath, f))]

df = pd.DataFrame()
for f in tqdm(onlyfiles):
    tqdm.write(f)
    csv = pd.read_csv(join(datapath, f))

    csv = csv.drop('seconds_elapsed', axis=1)

    csv= csv.set_index('time')

    cols = deepcopy(csv.columns.values)
    new_cols = [f.replace('.csv', "").lower() +"_"+col for col in cols if col != 'time']
    csv.columns = new_cols
    
    if df.empty:
        df=csv
    else:
        df = df.merge(csv, right_index=True, left_index=True,  how='outer')

df.to_csv('proc_data/1_full.csv', index=1)