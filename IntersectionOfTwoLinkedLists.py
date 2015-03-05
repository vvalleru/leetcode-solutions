# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        first = headA
        second = headB
        len_A = 0
        len_B = 0
        
        while first != None:
            len_A += 1
            first = first.next
        while second != None:
            len_B += 1
            second = second.next
        
        first = headA
        second = headB
        
        if len_A > len_B:
            len_A = len_A - len_B
            while len_A != 0:
               first = first.next
               len_A -= 1
        else:
            len_B = len_B - len_A
            while len_B != 0:
               second = second.next
               len_B -= 1        
        
        
        while first != second:
            first = first.next
            second = second.next
        
        return first