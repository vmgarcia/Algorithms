import random
import unittest

def quicksort(nums, left=None, right=None):
    '''
    Sort the range xs[fst, lst] in-place with vanilla QuickSort

    :param nums:  the list of numbers to sort
    :param right: the first index from xs to begin sorting from,
                must be in the range [0, len(xs))
    :param left: the last index from xs to stop sorting at
                must be in the range [fst, len(xs))
    :return:    nothing, the side effect is that xs[fst, lst] is sorted
    '''
    if left is None: left = 0
    if right is None: right = len(nums)-1
    if left >= right:
        return

    i, j = left, right
    pivot = nums[random.randint(left, right)]

    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, left, j)
    quicksort(nums, i, right)
  
class TestQuickSort(unittest.TestCase):
  def test_sort(self):
    to_sort = [5,4,2,67,1,46,4]
    quicksort(to_sort)
    self.assertEqual(to_sort, [1,2,4,4,5,46,67])

if __name__ == '__main__':
  unittest.main()