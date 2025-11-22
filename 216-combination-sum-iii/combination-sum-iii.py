class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(i,path,target):
            if len(path) > k:
                return
            if len(path) == k:
                if target == 0:
                    ans.append(path.copy()) 
                return
            for j in range(i , 10):
                path.append(j)
                backtrack(j + 1 ,path , target - j)
                path.pop()
        backtrack(1 , [] , n)
        return ans



