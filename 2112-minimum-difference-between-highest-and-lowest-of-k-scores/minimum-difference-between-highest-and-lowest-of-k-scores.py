class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left =  0
        ans = float("inf")
        for right in range(k-1 , len(nums)):
            ans = min(ans , nums[right] - nums[left])
            left += 1
        return ans


    # 1 4,7,9


