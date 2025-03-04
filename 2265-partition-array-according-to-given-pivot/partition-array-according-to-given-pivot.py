class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans=[]
        for i in range(len (nums)):
            if(nums[i]==pivot):
                ans.append(nums[i])
        
        for i in range(len(nums)):
            if (nums[i]>pivot):
                ans.append(nums[i])
        nums=nums[::-1]
        for i in range(len(nums)):
            if (nums[i]<pivot):
                ans.insert(0,nums[i])
        return ans