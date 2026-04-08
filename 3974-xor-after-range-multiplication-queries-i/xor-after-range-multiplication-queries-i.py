class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for li, ri, ki, vi in queries:
            idx = li
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % (10**9 + 7)
                idx += ki
        ans = nums[0]
        for num in nums[1:]:
            ans ^= num
        return ans 
