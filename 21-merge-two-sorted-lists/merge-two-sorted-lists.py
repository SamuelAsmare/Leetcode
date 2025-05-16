# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res , curr1 , curr2 = ListNode( None ) , list1 , list2
        res = ListNode(3)
        iterator = res
        while curr1 and curr2:
            if curr1.val>=curr2.val:
                iterator.next = curr2
                curr2 = curr2.next
            else:
                iterator.next = curr1
                curr1 = curr1.next
            iterator = iterator.next
        iterator.next = curr1 if curr1 else curr2           
        return res.next

