from infection_summary import *
from pandas import read_csv

# input dataset
D = read_csv(
      'input/private/sn/ego-Facebook/facebook_combined.txt',
      delimiter=' '
    ) \
    .to_numpy()

infection_summary(D, 'facebook')
