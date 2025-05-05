# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def count(head):
            i,curr=0,head
            while(curr.next):
                i+=1
                curr=curr.next
            return i
        def m(head):
            total=count(head)
            mid,curr = math.ceil(total/2),head
            for _ in range(mid):
                curr=curr.next
            return curr          
        return m(head)  