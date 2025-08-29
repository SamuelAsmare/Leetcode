class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans , path , initial_index = set() , [] , 0
        def backtrack(path , i , target): #
            if target==0:
                ans.add(tuple(sorted(path.copy())))
            if target<0:
                return 
            for sam in range(len(candidates)):
                path.append(candidates[sam])
                backtrack(path  , sam , target-candidates[sam])
                path.pop()
        backtrack(path , initial_index , target)
        return [list(tup) for tup in ans]