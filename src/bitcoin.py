from infection_summary import *
from pandas import read_csv

# input dataset
D = read_csv('input/bitcoinalpha.csv') \
    [['SOURCE', 'TARGET']].to_numpy()

infection_summary(D, 'bitcoinalpha')
