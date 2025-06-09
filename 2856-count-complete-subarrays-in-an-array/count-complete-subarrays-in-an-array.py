class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n , ans = len(set(nums)) , 0
        for i in range(len(nums)):
            fre = set([])
            for j in range(i,len(nums)):
                fre.add(nums[j])
                if(len(fre)==n):
                    ans+=1           
        return ans
                


