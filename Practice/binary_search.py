import unittest

def binary_search(nums, target):
  pass

class TestBinarySearch(unittest.TestCase):
  def test_binary_search(self):
    self.assertEqual(binary_search([0, 1, 2, 3, 4, 5, 6, 7], 3), 3)
  
  def test_binary_search_value_not_present(self):
    self.assertEqual(binary_search([0, 1, 2, 4, 5, 6, 7], 3), -1)

if __name__ == '__main__':
  unittest.main()