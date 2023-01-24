from infection_summary import *
from pandas import read_csv

# input dataset
D = read_csv(
      'input/private/instagram/Network for IC LT.txt', 
      delimiter=' ',
      header=None
    ) \
    .iloc[:, 0:2].to_numpy()

infection_summary(D, 'instagram')
