import unittest
from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
  graph = defaultdict(list)
  for (u, v, w) in edges:
    graph[u].append((w, v))
  
  min_distances = { f: 0 }
  parents = { f: None }
  visited = set()
  heap = [(0, f)]

  while heap:
    weight, current = heappop(heap)
    if current in visited: continue
    if current == t: break

    visited.add(current)
    for (neighbor_weight, neighbor) in graph[current]:
      last_weight = min_distances.get(neighbor, float('inf'))
      next_weight = neighbor_weight + weight
      if next_weight < last_weight:
        parents[neighbor] = current
        min_distances[neighbor] = next_weight
        heappush(heap, (next_weight, neighbor))
  
  if t in min_distances:
    path = []
    current = t
    while current:
      path.append(current)
      current = parents[current]
    path.reverse()
    return min_distances[t], path
    
  return float("inf"), None

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