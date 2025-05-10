# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()  
        def cycle(head):
            curr = head
            if not head:
                return False
            while curr.next:
                curr = curr.next
                if curr in seen:
                    return True
                seen.add(curr)
            return False
        print(seen)
        return cycle(head)
                
