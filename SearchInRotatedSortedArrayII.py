class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        for index in xrange(len(A)):
            if A[index] == target:
                return True
        return False