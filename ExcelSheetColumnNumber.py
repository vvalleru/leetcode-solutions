class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        result = 0
        for char in s:
            result *= 26;
            result += ord(char) - ord('A') + 1;
        return result