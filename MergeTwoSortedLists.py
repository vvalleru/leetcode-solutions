# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        bucket = []
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
                temp.next = None
            else:
                temp = l2
                l2 = l2.next
                temp.next = None
            bucket.append(temp)
        
        while l1 != None:
            temp = l1
            l1 = l1.next
            temp.next = None
            bucket.append(temp)

        while l2 != None:
            temp = l2
            l2 = l2.next
            temp.next = None
            bucket.append(temp)
        
        for i in xrange(0, len(bucket) - 1):
            bucket[i].next = bucket[i + 1]
        
        return bucket[0]