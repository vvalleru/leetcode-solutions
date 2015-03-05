class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        i = 0
        strNum = str(x)
        while i < len(strNum) / 2:
            if strNum[i] != strNum[len(strNum) - i - 1]:
                return False
            i += 1
        return True