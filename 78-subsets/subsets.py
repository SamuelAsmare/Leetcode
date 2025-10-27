class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp , ans = []  , []
        def backtrack(i):
            if i==len(nums):
                ans.append(temp.copy())
                return
            # pick
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()
            # dont pick
            backtrack(i+1)
        backtrack(0)
        return ans

