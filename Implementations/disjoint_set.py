import unittest

class DisjointSet:
  def __init__(self, keys=None):
    self.ranks = {}
    self.parents = {}
    if keys:
      self.add_many(keys)

  def add(self, key):
    if key not in self.parents:
      self.ranks[key] = 0
      self.parents[key] = key
  
  def add_many(self, keys):
    for key in keys:
      self.add(key)

  def find_root(self, key):
    if self.parents[key] is not key:
      self.parents[key] = self.find_root(self.parents[key])
    return self.parents[key]

  def union(self, key1, key2):
      root1, rank1 = self.find_root(key1), self.ranks[key1]
      root2, rank2 = self.find_root(key2), self.ranks[key2]

      if root1 == root2:
        return False

      if rank1 < rank2:
        self.parents[root1] = root2
      elif rank1 > rank2:
        self.parents[root2] = root1
      else:
        self.parents[root2] = root1
        self.ranks[root1] += 1
      return True
      
  def connected(self, key1, key2):
    return self.find_root(key1) == self.find_root(key2)

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