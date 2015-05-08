class RotateArray:
  # @param nums, a list of integer
  # @param k, num of steps
  # @return nothing, please modify the nums list in-place.
  def __init__(self, nums):
    self.nums = nums
    self.nums_len = len(nums)
    self.rotatedArray = [0] * len(nums)

  def rotate(self, K):
    if K > 0 and self.nums_len > 1:
      K = K % self.nums_len

      for index in xrange(K, self.nums_len):
        self.rotatedArray[index] = self.nums[index - K]

      for index in xrange(K):
        self.rotatedArray[index] = self.nums[index + K]
      if K == 1:
        self.rotatedArray[0] = self.nums[-1]

      self.nums = self.rotatedArray