class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen  = set()
        for item in nums:
            if item in seen: return item
            seen.add(item)
            