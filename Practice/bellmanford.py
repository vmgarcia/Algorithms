import unittest


"""
Time complexity: O(V*E)
Space complexity: O(V)
"""
def bellman_ford(graph, source):
  pass

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

 
  def test_bellman_ford_negative_cycle(self):

    graph = {
      'a': [(3, 'c')],
      'b': [(2, 'a')],
      'c': [(7, 'b'), (1, 'd')],
      'd': [(-1000, 'a')]
    }
    distance, predecessor = bellman_ford(graph, source='a')
    self.assertIsNone(distance)
    self.assertIsNone(predecessor)

if __name__ == '__main__':
  unittest.main()