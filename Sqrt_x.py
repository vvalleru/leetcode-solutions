class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0:
            return 0
        
        result = 1
        start = 1
        end = x - 1

        while start <= end:
            current = (start + end) / 2
            if current * current <= x:
                start = current + 1
                result = current
            else:
                end = current - 1

        return result