class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if i < n-1:
                if nums[i+1] == nums[i]:
                    nums[i] *= 2
                    nums[i+1] = 0
        ans = []
        for item in nums:
            if item != 0:
                ans.append(item)
        for _ in range(n-len(ans)):
            ans.append(0)
        return ans