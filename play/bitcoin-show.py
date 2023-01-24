import matplotlib.pyplot as plt
import networkx as nx
from pandas import read_csv

# build graph
#
G = nx.DiGraph()
G.add_edges_from(
  read_csv('input/bitcoinalpha.csv')
    [['SOURCE', 'TARGET']]
    .to_numpy()
)

# export graph visualization
#
plt.figure(figsize=(16, 9))
nx.draw_circular(**{
  'G': G,
  'edge_color': '#4444',
  'node_color': 'black',
  'node_size': 0.2,
  'width': 0.1,
  'arrowsize': 1,
  'arrowstyle': '->'
})
plt.savefig('output/bitcoinalpha_show.svg', **{
  'format': 'svg',
  'dpi': 800
})
