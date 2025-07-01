class Solution:
    def possibleStringCount(self, word: str) -> int:
        stack  , ans = [] , 1
        for item in word:
            if not stack:
                stack.append(item)
            elif stack[-1] != item:
                stack.append(item)
            else:
                ans += 1
        return ans
