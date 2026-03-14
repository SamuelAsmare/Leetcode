class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        def backtrack(path):
            if len(path) == n:
                ans.append(path)
                return
            for char in ["a" , "b" , "c"]:
                if not path or  path[-1] != char:
                    path = path + char
                    backtrack(path)
                    path = path[:-1]
        backtrack("")
        if len(ans) >= k:
            return ans[k-1]
        return ""
