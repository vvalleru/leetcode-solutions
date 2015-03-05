# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        elif head.next == None:
            return False
        
        slowPointer = fastPointer = head
        
        while fastPointer != None and fastPointer.next != None and fastPointer.next.next != None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True
        
        return False