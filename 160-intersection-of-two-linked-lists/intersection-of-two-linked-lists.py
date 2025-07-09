# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1,curr2 = headA , headB
        while curr1 != curr2:
            if curr1:
                curr1 = curr1.next
            else:
                curr1 = headB
            if curr2 :
                curr2 = curr2.next
            else:
                curr2 = headA
        return curr2
