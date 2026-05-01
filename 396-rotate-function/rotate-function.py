class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total , prev  , n = sum(nums) , 0 , len(nums)
        for i in range(n):
            prev += i*nums[i]
        ans = prev
        for i in range(1,n):
            prev = prev + total - n * nums[n-i]
            ans = max(ans , prev)
        return ans
            


