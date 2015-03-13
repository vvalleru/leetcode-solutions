class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n < 2:
            return 1

        fibList = [0] * n
        fibList[0] = 1
        fibList[1] = 1
        
        for index in xrange(2,n):
            fibList[index] = fibList[index-1] + fibList[index - 2]
            
        return fibList[n - 1] + fibList[n - 2]    