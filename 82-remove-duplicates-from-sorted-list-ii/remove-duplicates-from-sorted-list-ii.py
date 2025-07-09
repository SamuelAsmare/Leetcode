# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fre = defaultdict(int)
        curr = head
        while curr:
            fre[curr.val] +=1
            curr = curr.next
        curr  , dummy = head , ListNode(0)
        dummy.next  ,  prev = head , dummy
        while curr:
            if fre[curr.val] >= 2:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

    