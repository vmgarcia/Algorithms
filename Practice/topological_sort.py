import unittest
from collections import defaultdict, deque

def topological_sort(edges):
  pass

class TestTopologicalSort(unittest.TestCase):
  
  def test_simple_sort(self):
    edges = [[0, 1], [1, 2], [2, 3]]
    self.assertEqual(topological_sort(edges), [0, 1, 2,3])

  def test_three_roots(self):
    edges = [[1, 0], [2, 0], [3, 0]]
    self.assertEqual(topological_sort(edges), [1, 2, 3, 0])

  def test_bigger_dag(self):
    edges = [[5, 0], [4, 0], [4, 1], [1, 3], [2, 3], [5, 2]]
    self.assertEqual(topological_sort(edges), [5, 4, 2, 0, 1, 3])

  def test_cycle_detection(self):
    edges = [[0, 1], [1, 0], [1, 2]]
    self.assertEqual(topological_sort(edges), [])

if __name__ == '__main__':
  unittest.main()