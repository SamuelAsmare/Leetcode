# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def size(head):
            curr , size = head  , 0
            while curr:
                curr = curr.next
                size += 1
            return size 
        def remove(head , index):
            curr = head 
            prev = curr
            if index == 0:
                return curr.next # or the next node of the current node which is None
            for _ in range(index):
                prev = curr 
                curr = curr.next
            prev.next = curr.next
            return head
        size = size(head)
        return remove(head , size-n)
