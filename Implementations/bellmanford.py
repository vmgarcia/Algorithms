import unittest


"""
Time complexity: O(V*E)
Space complexity: O(V)
"""
def bellman_ford(graph, source):
    # Step 1: Prepare the distance and predecessor for each node
    distances = [{}, {}]
    predecessor = {}
    for node in graph:
      distances[0][node], distances[1][node] = float('inf'), float('inf')
      predecessor[node] = None

    distances[0][source] = 0
    distances[1][source] = 0

    # Step 2: Relax the edges
    for i in range(len(graph) - 1):
        for node in graph:
            for weight, neighbour in graph[node]:
                # If the distance between the node and the neighbour is lower than the current, store it
                if distances[i%2][neighbour] > distances[1-i%2][node] + weight:
                    distances[i%2][neighbour], predecessor[neighbour] = distances[1-i%2][node] + weight, node

    # Step 3: Check for negative weight cycles
    for node in graph:
        for weight, neighbour in graph[node]:
            assert distances[1-len(graph)%2][neighbour] <= distances[1-len(graph)%2][node] + weight, "Negative weight cycle."
 
    return distances[1-len(graph)%2], predecessor

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