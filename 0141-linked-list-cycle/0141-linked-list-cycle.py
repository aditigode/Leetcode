# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head, head
        
        #print(head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
            
        # slow -->  3   2   0   -4
        # fast -->  3   0   2   -4
        #print(slow,fast)
        if not fast or not fast.next or slow != fast:
            return False
        #print(slow,fast,head)
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return  True