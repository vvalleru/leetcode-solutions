class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start = 0
        end = len(num) - 1
        answer = -1
        if num[start] <= num[end]:
            answer = num[start]
        else:
            for index in xrange(end):
                if num[index] > num[index + 1]:
                    answer = num[index + 1]
        return answer