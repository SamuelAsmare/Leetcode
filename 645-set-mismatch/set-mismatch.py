class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans , s = [0,0] , set(nums)
        for i in range(1, len(nums) + 1):
            if (i not in s):
                ans[1] = i
            if nums.count(i)==2:
                ans[0] = i
            if 0 not in ans:
                return ans
            
        