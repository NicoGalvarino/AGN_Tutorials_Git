import pandas as pd
from collections import Counter

sub_df = pd.read_csv('sdss_sql_HW1_subclasses.csv', header=1)

QSOs = sub_df.loc[sub_df['class']=='QSO']
galaxies = sub_df.loc[sub_df['class']=='GALAXY']

print('Same number of objects as initial query?', sub_df.shape[0]==217)  # sanity check
print(' ')
print('Total number of QSOs: ', QSOs.shape[0])
print('QSO sub-classes: ',  Counter(QSOs['subClass']))
print(' ')
print('Total number of Galaxies: ', galaxies.shape[0])
print('GALAXY sub-classes: ',  Counter(galaxies['subClass']))