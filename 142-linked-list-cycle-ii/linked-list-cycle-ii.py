# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        rabbit = head
        while rabbit and rabbit.next :
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            if tortoise == rabbit:
                break
        else:
            return None
        tortoise = head
        while tortoise != rabbit:
            rabbit = rabbit.next
            tortoise = tortoise.next
        return rabbit
