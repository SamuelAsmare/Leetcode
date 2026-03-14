class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0
        result = ""

        def backtrack(path):
            nonlocal count, result

            if len(path) == n:
                count += 1
                if count == k:
                    result = path
                return

            for char in ["a", "b", "c"]:
                if not path or path[-1] != char:
                    backtrack(path + char)
                    if result:  # stop early if we found kth
                        return
        backtrack("")
        return result