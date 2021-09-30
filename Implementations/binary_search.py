import unittest

def binary_search(nums, target):
  left, right = 0, len(nums) - 1
  while left <= right:
    pivot = left + (right-left) // 2
    if nums[pivot] == target:
      return pivot
    if target < nums[pivot]:
      right = pivot - 1
    else:
      left = pivot + 1
  return -1

class TestBinarySearch(unittest.TestCase):
  def test_binary_search(self):
    self.assertEqual(binary_search([0, 1, 2, 3, 4, 5, 6, 7], 3), 3)
  
if __name__ == '__main__':
  unittest.main()