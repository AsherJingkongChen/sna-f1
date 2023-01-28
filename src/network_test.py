from pandas import read_csv
from infection_trend import *
from network_stats import *

# input dataset
D = {
  # 'bitcoinalpha':
  #   read_csv('input/bitcoinalpha.csv') \
  #     [['SOURCE', 'TARGET']].to_numpy(),

  # 'facebook': 
  #   read_csv(
  #     'input/private/sn/ego-Facebook/facebook_combined.txt',
  #     delimiter=' '
  #   ) \
  #   .to_numpy(),

  # 'instagram':
  #   read_csv(
  #     'input/private/instagram/Network for IC LT.txt', 
  #     delimiter=' ',
  #     header=None
  #   ) \
  #   .iloc[:, 0:2].to_numpy(),

  # 'org_l':
  #   read_csv('input/private/organizational/L1Anonymized.csv', header=None) \
  #     .to_numpy(),

  # 'org_m':
  #   read_csv('input/private/organizational/M1Anonymized.csv', header=None) \
  #     .to_numpy(),

  # 'org_s':
  #   read_csv('input/private/organizational/S1Anonymized.csv', header=None) \
  #     .to_numpy(),
  
  # 'slashdot':
  #   read_csv('input/private/slashdot.csv') \
  #     [['SOURCE', 'TARGET']].to_numpy(),

  # 'github':
  #   read_csv('input/private/github/github_edges_1.csv') \
  #     [['id_1', 'id_2']].to_numpy(),

  # 'ws_graph_k15':
  #   nx.watts_strogatz_graph(n=2500, k=15, p=0.3, seed=255).edges,
  
  # 'ws_graph_k25':
  #   nx.watts_strogatz_graph(n=2500, k=25, p=0.3, seed=255).edges,
  
  # 'ws_graph_k35':
  #   nx.watts_strogatz_graph(n=1000, k=35, p=0.3, seed=255).edges
}

# for subject, data in D.items():
#   stats(subject, data)

# for subject, data in D.items():
#   output_csv(subject, D[subject])
#   output_svg(subject)

output_ws_heatmap_csv()
output_ws_heatmap_svg()

# output_svg_all(D.keys())
