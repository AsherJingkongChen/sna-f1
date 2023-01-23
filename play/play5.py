import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
from collections import Counter
from pandas import read_csv

random.seed(255)
sample_count = 50

# input dataset
D = read_csv('input/private/slashdot.csv') \
    [['SOURCE', 'TARGET']].to_numpy()

# build graph
#
# check the graph scale
#
G = nx.Graph()
G.add_edges_from(D)
stats = {
  'node_count': len(G.nodes),
  'avg_cluster': nx.average_clustering(G)
}
print(stats)

# X: infection threshold
# Y: average infected ratio
#
X = np.linspace(0, 0.1, 10 + 1)
Y = []

for infection_th in X:
  infected_ratio_sum = 0

  for _ in range(sample_count):
    for node, attr in G.nodes.data():
      attr['infected'] = False

    # mark infected nodes
    #
    origin = random.choice(list(G.nodes))
    G.nodes[origin]['infected'] = True

    # spread infection
    #
    for nodes in nx.bfs_layers(G, [origin]):
      for node in nodes:
        S = Counter(
          G.nodes[nbr]['infected']
          for nbr in G.adj[node].keys()
        )
        neighbor_infected_ratio = \
          S[True] / (S[True] + S[False])
        if neighbor_infected_ratio > infection_th:
          G.nodes[node]['infected'] = True

    S = Counter(node[1]['infected'] for node in G.nodes.data())
    infected_ratio_sum += S[True] / (S[True] + S[False])

  y = infected_ratio_sum / sample_count
  print(y)
  Y.append(y)

plt.figure(figsize=(14, 7))
plt.plot(X, Y, color='#B80', linewidth=2)
plt.grid(which='both', alpha=0.3)
plt.xlabel('Infection threshold')
plt.ylabel('Infected ratio (average)')
plt.title(f'Infection mode on slashdot, '\
          f'average clustering = {stats["avg_cluster"]}')

plt.savefig('output/infection_slashdot.svg', **{
  'format': 'svg',
  'dpi': 800
})
