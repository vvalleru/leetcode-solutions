class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        while len(s) > 0 and s[-1] == ' ':
            s = s[:-1]
        
        index = len(s) - 1
        
        while index >= 0 and s[index] != ' ':
            index -= 1
        index += 1
        return len(s) - index