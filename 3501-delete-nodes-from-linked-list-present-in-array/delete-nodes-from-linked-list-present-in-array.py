class Solution:
    def modifiedList(self, nums, head):
        remove_set = set(nums)  
        dummy = ListNode(0, head)
        curr = dummy

        while curr and curr.next:
            if curr.next.val in remove_set:
                curr.next = curr.next.next  
            else:
                curr = curr.next

        return dummy.next
