class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxsum=0
        maxelement=max(nums)
        while(k>0):
            maxsum+=maxelement
            maxelement=maxelement+1
            k-=1
        return maxsum

