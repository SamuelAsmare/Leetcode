class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum=float("-inf")
        subarr=[nums[i:j+1] for i in range (len(nums)) for j in range (i,len(nums))]
        for i in range (len(subarr)):
            if(all(subarr[i][j] < subarr[i][j + 1] for j in range(len(subarr[i]) - 1))):
                if(sum(subarr[i])>maxsum):
                    maxsum=sum(subarr[i])
        return maxsum


        