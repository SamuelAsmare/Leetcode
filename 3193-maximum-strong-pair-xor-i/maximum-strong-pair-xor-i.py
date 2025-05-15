class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxor = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                if (abs(nums[i] - nums[j]) <= min(nums[i],nums[j])):
                    maxor = max(maxor , nums[i] ^ nums[j])
        return maxor