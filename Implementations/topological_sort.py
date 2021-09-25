from typing import DefaultDict


import unittest
from collections import defaultdict, deque

def topological_sort(edges):
  graph = defaultdict(list)
  in_degree = defaultdict(int)

  for u, v in edges:
    graph[u].append(v)
    if u not in in_degree:
      in_degree[u] = 0
    in_degree[v] += 1
  
  q = deque()
  for node, degree in in_degree.items():
    if degree == 0:
      q.append(node)
  visited_count = 0

  sorted_nodes = []

  while q:
    node = q.popleft()
    sorted_nodes.append(node)
    for neighbor in graph[node]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor] == 0:
        q.append(neighbor)
    visited_count += 1
  return sorted_nodes


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
if __name__ == '__main__':
  unittest.main()