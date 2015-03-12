class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        times = 32
        while times != 0:
            result = result << 1
            if n&1 == 1:
                result = result ^ 1
            n = n >> 1
            times -= 1
        return result