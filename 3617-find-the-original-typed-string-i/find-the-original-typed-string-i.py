class Solution:
    def possibleStringCount(self, word: str) -> int:
        end  , ans = "" , 1
        for item in word:
            if not end:
                end = item
            elif end != item:
                end = item
            else:
                ans += 1
        return ans
