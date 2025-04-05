class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n,Sum=len(nums),0
        for i in range(1,n+1):
            for each in combinations(nums,i):
                temp=each[0]
                for k in range(len(each)-1):
                    temp^=each[k+1]
                Sum+=temp
        return Sum
