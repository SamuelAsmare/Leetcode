class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if(k==1):
            nums.sort()
            for i in range(len(nums)-1,-1,-1):
                if(nums.count(nums[i])==1):
                    return nums[i]
        if(k==len(nums)):
            nums.sort()
            return nums[-1]
        if(nums.count(nums[-1])==1):
            if(nums.count(nums[0])==1):
                return max(nums[0],nums[-1])
            else:
                return nums[-1]
        if(nums.count(nums[0])==1):
            if(nums.count(nums[-1])==1):
                return max(nums[0],nums[-1])
            else:
                return nums[0]
        return -1
        
