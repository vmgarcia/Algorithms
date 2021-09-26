import unittest


"""
Time complexity: O(V*E)
Space complexity: O(V)
"""
def bellman_ford(graph, source):
    # Step 1: Prepare the distance and predecessor for each node
    previous = {}
    current = {}
    predecessor = {}
    for node in graph:
      previous[node], current[node] = float('inf'), float('inf')
      predecessor[node] = None

    previous[source] = 0
    current[source] = 0
    # Step 2: Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for weight, neighbour in graph[node]:
                # If the distance between the node and the neighbour is lower than the current, store it
                if current[neighbour] > previous[node] + weight:
                    current[neighbour], predecessor[neighbour] = previous[node] + weight, node
        current, previous = previous, current

    # Step 3: Check for negative weight cycles
    for node in graph:
        for weight, neighbour in graph[node]:
            assert current[neighbour] <= current[node] + weight, "Negative weight cycle."
 
    return current, predecessor

class TestBellmanFord(unittest.TestCase):
  def test_bellman_ford(self):
    graph = {
      'a': [(-1, 'b'), (4, 'c')],
      'b': [(3, 'c'), (2, 'd'), (2, 'e')],
      'c': [],
      'd': [(1, 'b'), (5, 'c')],
      'e': [(-3, 'd')]
    }
    distance, predecessor = bellman_ford(graph, source='a')
    self.assertDictEqual(distance, {'a': 0, 'b': -1, 'c': 2, 'd': -2, 'e': 1})
    self.assertDictEqual(predecessor, {'a': None, 'b': 'a', 'c': 'b', 'd': 'e', 'e': 'b'})
 
  def test_bellman_ford_2(self):

    graph = {
      'a': [(3, 'c')],
      'b': [(2, 'a')],
      'c': [(7, 'b'), (1, 'd')],
      'd': [(6, 'a')]
    }
    distance, predecessor = bellman_ford(graph, source='a')
    self.assertDictEqual(distance, {'a': 0, 'b': 10, 'c': 3, 'd': 4})
    self.assertDictEqual(predecessor, {'a': None, 'b': 'c', 'c': 'a', 'd': 'c'})

if __name__ == '__main__':
  unittest.main()