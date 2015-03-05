class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        for i in xrange(1, len(num) - 1):
            if num[i - 1] < num[i] > num[i + 1]:
                return i
        if num[0] > num[-1]:
            return 0
        return len(num) - 1