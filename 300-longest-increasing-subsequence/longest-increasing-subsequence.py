class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [10,9,2,5,3,7,101,18]
        n = len(nums)
        gech = [1] * n
        for i in range(n-1 , -1 , -1 ):
            for j in range(i+1 , n):
                if nums[i] < nums[j]:
                    gech[i] = max(gech[i] , gech[j] + 1)
        return max(gech)
