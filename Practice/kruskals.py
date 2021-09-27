import unittest

"""
Time complexity: O(E * LogE)
Space complexity: O(V)
"""

class DisjointSet:
  def __init__(self, keys=None):
    self.parents = {}
    self.ranks = {}
    if keys:
      self.add_many(keys)

  def add(self, key):
    if key not in self.parents:
      self.parents[key] = key
      self.ranks[key] = 0
  
  def add_many(self, keys):
    for key in keys:
      self.add(key)

  def find_root(self, key):
    if self.parents[key] == key:
      return key
    self.parents[key] = self.find_root(self.parents[key])
    return self.parents[key]

  def union(self, key1, key2):
    root1 = self.find_root(key1)
    root2 = self.find_root(key2)
    rank1 = self.ranks[root1]
    rank2 = self.ranks[root2]
    if root1 == root2:
      return
    elif rank1 > rank2:
      self.parents[root2] = root1
    elif rank1 < rank2:
      self.parents[root1] = root2
    else:
      self.parents[root2] = root1
      self.ranks[root1] += 1
    return

  def connected(self, key1, key2):
    return self.find_root(key1) == self.find_root(key2)


def kruskals(n, edges):
  pass

class TestKruskals(unittest.TestCase):
  def test_kruskals(self):
    graph = {
      'A': {'B': 2, 'C': 3},
      'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
      'C': {'A': 3, 'B': 1, 'F': 5},
      'D': {'B': 1, 'E': 1},
      'E': {'B': 4, 'D': 1, 'F': 1},
      'F': {'C': 5, 'E': 1, 'G': 1},
      'G': {'F': 1},
    }

    edges = []
    for a in graph:
      for b, w in graph[a].items():
        edges.append((w, a, b))
    self.assertEqual(kruskals(len(graph), edges), 7)
if __name__ == "__main__":
  unittest.main()