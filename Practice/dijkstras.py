import unittest
from collections import defaultdict, deque
from heapq import heappop, heappush

def dijkstra(edges, f, t):
  pass

class TestDijkstras(unittest.TestCase):

  def test_get_shortest_path(self):
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]
    self.assertEqual(dijkstra(edges, "A", "E"), (14, ['A', 'B', 'E']))
    self.assertEqual(dijkstra(edges, "A", "F"), (11, ['A', 'D', 'F']))


if __name__ == "__main__":
  unittest.main()