class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        sum1=0
        count=0
        for i in range(len(nums)-1):
            sum2=0
            sum1=sum1+nums[i]
            for j in range(i+1,len(nums),+1):
                sum2=sum2+nums[j]
            if(sum1-sum2)%2==0:
                count=count+1
        return count
        