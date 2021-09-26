import unittest
from heapq import heappush, heappop, heapify

def prims(graph, start):
  pass

class TestPrims(unittest.TestCase):
  def test_prims(self):
    graph = {
      'A': [(2, 'B'), (3, 'C')],
      'B': [(2, 'A'), (1, 'C'), (1, 'D'), (4, 'E')],
      'C': [(3, 'A'), (1, 'B'), (5, 'F')],
      'D': [(1, 'B'), (1, 'E')],
      'E': [(4, 'B'), (1, 'D'), (1, 'F')],
      'F': [(5, 'C'), (1, 'E'), (1, 'G')],
      'G': [(1, 'F')],
    }

    self.assertEqual(prims(graph, 'A'), 7)

if __name__ == "__main__":
  unittest.main()