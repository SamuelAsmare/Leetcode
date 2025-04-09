class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums=list(set(nums))
        nums.sort()
        if(k>nums[0]):
            return -1
        counter=len(nums)-1
        if(nums[0]==k):
            return counter
        else:
            return counter+1
       


        
        
        

        
        

