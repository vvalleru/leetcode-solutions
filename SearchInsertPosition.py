class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        n = len(A)
        beg = 0
        end = n - 1
        result = -1
        
        while (beg <= end):
            mid = (beg + end) / 2
            if (A[mid] <= target):
                beg = mid + 1
                result = mid
            else:
                end = mid - 1
        if A[result] == target:
            return result
        else:
            return result + 1