# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        
        node = head
        while node:
            node = node.next
            count += 1
        #print("count",count)
        if count == 1:
            return None
        count = count - n
        #print("count start",count )
        c = 1
        node = head
        prev = node
        while c < count:
            prev = node
            node = node.next
            c += 1
        #print("c",c)
        #print(node,prev)
        if c > 1:
            prev.next = node.next
        else:
            head = node.next
        return head
        