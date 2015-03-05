class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        n = len(num)
        stack = []
        for i in xrange(0, n):
            stack.append(num[i])
            if len(stack) == 1:
                continue
            if stack[-1] != stack[-2]:
                stack.pop()
                stack.pop()
        return stack[-1]