import unittest
import RotateArray

class RotateArrayTest(unittest.TestCase):
  def testZeroRotations(self):
    nums = [1,2,3,4,5]
    K = 0
    ra = RotateArray.RotateArray(nums)
    ra.rotate(K)
    expected = [1,2,3,4,5]
    actual = ra.nums
    self.assertSequenceEqual(actual, expected)

  def testThreeRotations(self):
    nums = [1,2,3,4,5]
    K = 3
    ra = RotateArray.RotateArray(nums)
    ra.rotate(K)
    expected = [3,4,5,1,2]
    actual = ra.nums
    self.assertSequenceEqual(actual, expected)

  def testMoreThanLengthOfArray(self):
    nums = [1,2,3,4,5]
    K = 6
    ra = RotateArray.RotateArray(nums)
    ra.rotate(K)
    expected = [5,1,2,3,4]
    actual = ra.nums
    self.assertSequenceEqual(actual, expected)

  def testEmptyArray(self):
    nums = []
    K = 3
    ra = RotateArray.RotateArray(nums)
    ra.rotate(K)
    expected = []
    actual = ra.nums
    self.assertSequenceEqual(actual, expected)

  def testSingleElementArray(self):
    nums = [1]
    K = 4
    ra = RotateArray.RotateArray(nums)
    ra.rotate(K)
    expected = [1]
    actual = ra.nums
    self.assertSequenceEqual(actual, expected)