import unittest

class DisjointSet:
  def __init__(self, keys=None):
    pass

  def add(self, key):
    pass
  
  def add_many(self, keys):
    pass

  def find_root(self, key):
    pass

  def union(self, key1, key2):
    pass
    
  def connected(self, key1, key2):
    pass


class TestDisjointSet(unittest.TestCase):

  def test_union(self):
    disjoint_set = DisjointSet(keys=['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'c1'])
    disjoint_set.union('a1', 'a2')
    disjoint_set.union('a2', 'a3')
    disjoint_set.union('a4', 'a1')
    self.assertTrue(disjoint_set.connected('a4', 'a3'))
    self.assertTrue(disjoint_set.connected('a2', 'a1'))
    self.assertEqual(disjoint_set.ranks['a1'], 2)
    self.assertEqual(disjoint_set.parents['a3'], 'a1')
  
  def test_different_components(self):
    disjoint_set = DisjointSet(keys=['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'c1'])
    disjoint_set.union('a1', 'a2')
    disjoint_set.union('a2', 'a3')
    disjoint_set.union('a4', 'a1')
    disjoint_set.union('b1', 'b2')
    self.assertTrue(disjoint_set.connected('a4', 'a3'))
    self.assertFalse(disjoint_set.connected('a4', 'b2'))
    self.assertFalse(disjoint_set.connected('b1', 'c1'))
    self.assertTrue(disjoint_set.connected('b1', 'b2'))

  
if __name__ == '__main__':
  unittest.main()