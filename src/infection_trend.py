import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
from pandas import DataFrame, read_csv
from collections import Counter

def output_csv(subject, data):
  random.seed(255)
  sample_count = 30

  # build graph
  #
  # check the graph scale
  #
  G = nx.Graph()
  G.add_edges_from(data)

  # X: infection threshold
  # Y: average infected ratio
  #
  X = np.linspace(0, 0.2, 20 + 1)
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
      old_infection_scale = 0
      infected_nodes = set([origin])

      while len(infected_nodes) != old_infection_scale:
        old_infection_scale = len(infected_nodes)
        new_infected_nodes = infected_nodes.copy()

        for infected_node in infected_nodes:
          for nearby_node in G.adj[infected_node].keys():
            if G.nodes[nearby_node]['infected']:
              continue

            S = Counter(
              G.nodes[nbr]['infected']
              for nbr in G.adj[nearby_node].keys()
            )
            if S[True] / (S[True] + S[False]) > infection_th:
              G.nodes[nearby_node]['infected'] = True
              new_infected_nodes.add(nearby_node)

        infected_nodes = new_infected_nodes

      S = Counter(node[1]['infected'] for node in G.nodes.data())
      infected_ratio_sum += S[True] / (S[True] + S[False])

    y = infected_ratio_sum / sample_count
    Y.append(y)
    print(y)

  DataFrame(data={'X': X, 'Y': Y}) \
    .to_csv(f'output/infection_{subject}.csv')

def output_svg(subject):
  data = read_csv(f'output/infection_{subject}.csv')
  plt.figure(figsize=(14, 7))
  plt.plot(data['X'], data['Y'], color='#B80', linewidth=2)
  plt.grid(which='both', alpha=0.3)
  plt.xlabel('Infection threshold')
  plt.ylabel('Infected ratio (average)')
  plt.xticks(data['X'])
  plt.yticks(np.linspace(0, 1, 10 + 1))
  plt.title(f'Infection mode on {subject}')

  plt.savefig(f'output/infection_{subject}.svg', **{
    'format': 'svg',
    'dpi': 800
  })
