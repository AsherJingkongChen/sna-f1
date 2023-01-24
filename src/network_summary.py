from pandas import read_csv
from infection_trend import *
from network_stats import *

# input dataset
D = {
  'bitcoinalpha':
    read_csv('input/bitcoinalpha.csv') \
      [['SOURCE', 'TARGET']].to_numpy(),

  'facebook': 
    read_csv(
      'input/private/sn/ego-Facebook/facebook_combined.txt',
      delimiter=' '
    ) \
    .to_numpy(),

  'instagram':
    read_csv(
      'input/private/instagram/Network for IC LT.txt', 
      delimiter=' ',
      header=None
    ) \
    .iloc[:, 0:2].to_numpy(),

  'org_l':
    read_csv('input/private/organizational/L1Anonymized.csv', header=None) \
      .to_numpy(),

  'org_m':
    read_csv('input/private/organizational/M1Anonymized.csv', header=None) \
      .to_numpy(),

  'org_s':
    read_csv('input/private/organizational/S1Anonymized.csv', header=None) \
      .to_numpy(),
  
  'slashdot':
    read_csv('input/private/slashdot.csv') \
      [['SOURCE', 'TARGET']].to_numpy(),

  'github':
    read_csv('input/private/github/github_edges_1.csv') \
      [['id_1', 'id_2']].to_numpy(),
}

for subject, data in D.items():
  stats(subject, data)

output_csv('bitcoinalpha', D['bitcoinalpha'])
output_csv('facebook', D['facebook'])
output_csv('instagram', D['instagram'])
output_csv('org_l', D['org_l'])
output_csv('org_m', D['org_m'])
output_csv('org_s', D['org_s'])
output_csv('slashdot', D['slashdot'])
output_csv('github', D['github'])
