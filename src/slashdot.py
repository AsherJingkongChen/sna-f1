from infection_summary import *
from pandas import read_csv

# input dataset
D = read_csv('input/private/slashdot.csv') \
    [['SOURCE', 'TARGET']].to_numpy()

infection_summary(D, 'slashdot')
