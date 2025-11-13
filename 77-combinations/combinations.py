class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        result = []
        def backtrack(i,path):
            if i >= len(nums):
                return
            path.append(nums[i])
            if len(path)==k:
                result.append(path.copy())
            for j in range(i+1,len(nums)):
                backtrack(j,path)
                path.pop()
        for i in range(len(nums)):
            backtrack(i,[])
        return result

 