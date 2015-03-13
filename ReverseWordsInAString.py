class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        charList = self.reverse(list(s))
        start = 0
        answer = ""
        while start < len(charList):
            while start < len(charList) and charList[start] == " ":
                start += 1
            end = start
            while end < len(charList) and charList[end] != " ":
                end += 1
            answer += " " + "".join(self.reverse(charList[start:end]))
            start = end

        return answer.strip()

    def reverse(self, charList):
        start = 0
        end = len(charList) - 1
        while start < end:
            char = charList[start]
            charList[start] = charList[end]
            charList[end] = char
            start += 1
            end -= 1
        return charList