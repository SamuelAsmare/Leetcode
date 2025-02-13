class Solution:
    def maxLength(self, nums: List[int]) -> int:
        maxsize=float("-inf")
        subarr=[nums[i:j+1] for i in range (len(nums)) for j in range(i,len(nums))]
        for i in range (len(subarr)):
            if(math.prod(subarr[i])==reduce(gcd,subarr[i])*reduce(lcm,subarr[i])):
                if(maxsize<len(subarr[i])):
                    maxsize=len(subarr[i])
        return maxsize