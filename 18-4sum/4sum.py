class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set([])
        for i in range(n):
            for j in range(i+1,n):
                rem  = target - (nums[i] + nums[j])
                left , right = j + 1 , n-1
                while left < right:
                    if nums[left] + nums[right] > rem :
                        right -= 1
                    elif nums[left] + nums[right] < rem:
                        left += 1
                    else:
                        ans.add((nums[i] , nums[j] , nums[left] , nums[right]))
                        left += 1
                        right -= 1
        return [list(item) for item in ans]
