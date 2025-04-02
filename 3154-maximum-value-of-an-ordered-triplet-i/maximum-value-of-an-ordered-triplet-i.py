class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n,maxval=len(nums),0

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if(maxval<(nums[i]-nums[j])*nums[k]):
                        maxval=(nums[i]-nums[j])*nums[k]
        return maxval