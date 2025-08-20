class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        curr = head
        prev = None
        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        return prev
        