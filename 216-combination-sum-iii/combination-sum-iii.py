class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [1,2,3,4,5,6,7,8,9]
        ans = []
        def backtrack(i,path,target):
            if len(path) > k:
                return
            if len(path) == k:
                if target == 0:
                    ans.append(path.copy()) 
                return
            for j in range(i , 9):
                path.append(arr[j])
                backtrack(j + 1 ,path , target - arr[j])
                path.pop()
        backtrack(0 , [] , n)
        return ans



