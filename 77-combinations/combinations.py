class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        temp , ans = [] , []
        def backtrack(i):
            if len(temp) == k:
                ans.append(temp.copy())
                return 
            if i == n:
                return
            # pick
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()
            # dont pick
            backtrack(i+1)
        backtrack(0)
        return ans
