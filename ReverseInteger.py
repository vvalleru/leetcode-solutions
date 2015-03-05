class Solution:
    # @return an integer
    def reverse(self, x):
        if x >= 0:
            y = int(str(x)[::-1])
            if y > 2147483647:
                return 0
            return y
        if x < 0 :
            y = int(str(x)[:0:-1]) * -1
            if y < -2147483648:
                return 0
            return y