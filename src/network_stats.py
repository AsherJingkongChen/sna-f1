import networkx as nx
import numpy as np

def stats(subject, data):
  G = nx.Graph()
  G.add_edges_from(data)
  print(subject)
  print(
    '\n'.join([
      str(k) + ': ' + str(v)
      for k, v in
        {
          'node_count': len(G.nodes),
          'edge_count': len(G.edges),
          'avg_cluster': nx.average_clustering(G),
          'avg_degree': np.mean(np.array([v for k, v in nx.degree(G)])),
          'density': nx.density(G),
          # 'avg_conn': nx.average_node_connectivity(G)
        }.items()
    ])
  )
