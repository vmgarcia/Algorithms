import unittest

"""
Time complexity: O(E * LogE)
Space complexity: O(V)
"""
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