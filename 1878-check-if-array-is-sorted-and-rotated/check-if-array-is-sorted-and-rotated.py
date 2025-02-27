class Solution:
    def check(self, nums: List[int]) -> bool:
        temp=list(nums)
        nums.sort()
        n=len(nums)
        yes=False
        while(n>0):
            nums=[nums[-1]]+nums[:-1]
            print(nums)
            if(nums==temp):
                yes=True
                break
            n=n-1
        return yes