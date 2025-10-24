# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less , greater = ListNode(0) , ListNode(1)
        lesspointer , greaterpointer = less , greater
        curr = head
        while curr:
            if curr.val < x:
                lesspointer.next = curr
                lesspointer = lesspointer.next
            else:
                greaterpointer.next = curr
                greaterpointer = greaterpointer.next
            curr = curr.next
        greaterpointer.next = None
        lesspointer.next = greater.next
        return less.next