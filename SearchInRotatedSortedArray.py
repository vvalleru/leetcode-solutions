class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        pos = 0

        for index in xrange(len(A) - 1):
            if A[index] > A[index + 1]:
                pos = index
                break

        firstStart = 0
        firstEnd = pos
        secondStart = pos + 1
        secondEnd = len(A) - 1
        start = 0
        end = len(A)

        if A[firstStart] <= target <= A[firstEnd]:
            start = firstStart
            end = firstEnd
        else:
            start = secondStart
            end = secondEnd

        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

sol = Solution()
print sol.search([1], 1)