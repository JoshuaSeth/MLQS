import pandas as pd

df=pd.read_csv('proc_data/1_full.csv')

df['annotation_text'] = df['annotation_text'].fillna(method='bfill')

df.insert(1, 'annotation_text', df.pop('annotation_text'))


df['annotation_text'] = df['annotation_text'].fillna(method='ffill')

# Replace n with 0
df['annotation_text'] = df['annotation_text'].str.replace('n', '0')

df['annotation_text'] = df['annotation_text'].fillna('0')

df['target'] = df['annotation_text'].astype(int)

df = df.drop('annotation_text', axis=1)

df.to_csv('proc_data/2_filled.csv', index=False)