class Solution:
    # @return a string
    def convertToTitle(self, num):
        result = ''

        while num > 0:
            num -= 1
            result = chr(65 + num % 26) + result
            num /= 26
        
        return result