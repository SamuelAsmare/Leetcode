class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left,ans,right=0,0,len(nums)-1
        while(right>left):
            if(nums[left]+nums[right]<target):
                ans+=(right-left)
                left+=1
            else:
                right-=1
        return ans
        