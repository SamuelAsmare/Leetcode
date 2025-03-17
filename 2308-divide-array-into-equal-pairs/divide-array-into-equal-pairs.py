class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        arr=set(nums)
        for i in arr:
            if (nums.count(i)%2!=0):
                return False
        return True