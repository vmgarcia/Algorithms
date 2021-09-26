import unittest
from disjoint_set import DisjointSet
"""
Time complexity: O(E * LogE)
Space complexity: O(V)
"""
def kruskals(n, edges):
  ds = DisjointSet()
  edge_count = 0
  total_weight = 0
  for w, a, b in sorted(edges):
    ds.add(a)
    ds.add(b)
    if ds.union(a, b):
      edge_count += 1
      total_weight += w
      if edge_count == n-1:
        break
  return total_weight


class TestKruskals(unittest.TestCase):
  def test_kruskals(self):
    graph = {
      'A': [(2, 'B'), (3, 'C')],
      'B': [(2, 'A'), (1, 'C'), (1, 'D'), (4, 'E')],
      'C': [(3, 'A'), (1, 'B'), (5, 'F')],
      'D': [(1, 'B'), (1, 'E')],
      'E': [(4, 'B'), (1, 'D'), (1, 'F')],
      'F': [(5, 'C'), (1, 'E'), (1, 'G')],
      'G': [(1, 'F')],
    }

    edges = []
    for a in graph:
      for w, b in graph[a]:
        edges.append((w, a, b))
    self.assertEqual(kruskals(len(graph), edges), 7)
if __name__ == "__main__":
  unittest.main()