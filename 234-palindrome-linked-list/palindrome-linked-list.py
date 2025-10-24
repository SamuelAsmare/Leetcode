# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 2. reversing the second half then compare 
        # get the second half
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next  = prev
            prev = curr
            curr = temp
        # compare 
        first = head
        second = prev
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True



