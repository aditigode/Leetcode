# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head2 = list2
        
        while head2.next:
            head2 = head2.next
        
        
        count = 0
        head1 = list1
        
        while count <= b:
            if count == a-1:
                link1 = head1
            elif count == b:
                link2 = head1
            head1 = head1.next
            count += 1
            
        link1.next = list2
        head2.next = link2.next
        
        return list1
            