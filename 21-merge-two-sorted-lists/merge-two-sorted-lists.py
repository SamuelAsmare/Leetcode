# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1
        if not list1 and not list2:
            return
        pointer1 , pointer2 = list1 , list2
        if list1.val > list2.val:
            merged = pointer2
            pointer2 = pointer2.next
        else:
            merged = pointer1
            pointer1 = pointer1.next
        ans = merged
        while pointer1 and pointer2:
            if pointer1.val > pointer2.val:
                merged.next = pointer2
                merged = merged.next
                pointer2 = pointer2.next
            else:
                merged.next = pointer1
                merged = merged.next
                pointer1 = pointer1.next
        if pointer2:
            merged.next = pointer2
        if pointer1:
            merged.next = pointer1
        return ans



