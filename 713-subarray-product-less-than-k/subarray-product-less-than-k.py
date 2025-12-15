class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left , n , ans   = 0 , len(nums) , 0
        prod   =  1  
        for right in range(n):
            prod *= nums[right]
            while prod >= k and left < n:
                prod = prod//nums[left]
                left += 1
            ans += (right - left + 1)
        return ans

            





