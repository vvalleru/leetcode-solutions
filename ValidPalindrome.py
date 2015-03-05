class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
    
        while start <= end:
            if ((ord(s[start]) >= 48 and ord(s[start]) <= 57) or (ord(s[start]) >= 65 and ord(s[start]) <= 90) or (ord(s[start]) >= 97 and ord(s[start]) <= 122)) and\
                ((ord(s[end]) >= 48 and ord(s[end]) <= 57) or (ord(s[end]) >= 65 and ord(s[end]) <= 90) or (ord(s[end]) >= 97 and ord(s[end]) <= 122)):
                if s[start].lower() != s[end].lower():
                    break
                else:
                    start += 1
                    end -= 1
            else:
                if (ord(s[start]) >= 48 and ord(s[start]) <= 57) or (ord(s[start]) >= 65 and ord(s[start]) <= 90) or (ord(s[start]) >= 97 and ord(s[start]) <= 122):
                    end -= 1
                else:
                    start += 1
    
        else:
            return True
        return False