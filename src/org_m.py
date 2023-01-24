from infection_summary import *
from pandas import read_csv

# input dataset
D = read_csv('input/private/organizational/M1Anonymized.csv', header=None) \
    .to_numpy()

infection_summary(D, 'org_m')