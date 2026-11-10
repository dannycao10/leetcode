# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummyNode = ListNode(None, head)
        first, second = dummyNode, head

        while n:
            second = second.next
            n -= 1
        
        while second:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        return dummyNode.next