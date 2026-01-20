class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        new=[]
        for i in range(len(nums)):
            found=False
            for j in range (nums[i]+1):
                if((j | j+1) ==nums[i]):
                    new.append(j)
                    found=True
                    break
            if(not found ):
                new.append(-1)
        return new