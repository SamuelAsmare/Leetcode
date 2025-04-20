class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fre,n=Counter(nums),0
        for i in range(len (nums)):
            if fre[nums[i]]>=2:
                n=nums[i]
                break
        return n 
