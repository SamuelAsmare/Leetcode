class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(i,path,target):
            if target == 0:
                ans.append(path.copy())
                return 
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[j])
                backtrack(j + 1 ,path , target - candidates[j])
                item = path.pop()
        backtrack(0 , [] , target)
        return ans