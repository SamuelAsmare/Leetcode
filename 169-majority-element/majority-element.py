class Solution:
    def majorityElement(self, nums: List[int]) -> int:
     max=0 
     newindex = 0
     fre=Counter(nums)
     for i in range(len(nums)):
        if(fre[nums[i]]>max):
           max=fre[nums[i]]
           newindex=i
     return nums[newindex] 
        