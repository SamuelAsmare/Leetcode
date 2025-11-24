class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i - 1  >= 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j - 1  >= i+1 and nums[j] == nums[j-1]:
                    continue
                rem  = target - (nums[i] + nums[j])
                left , right = j + 1 , n-1
                while left < right:
                    if nums[left] + nums[right] > rem :
                        right -= 1
                    elif nums[left] + nums[right] < rem:
                        left += 1
                    else:
                        ans.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return ans
