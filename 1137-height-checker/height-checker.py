class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected , ans  = sorted(heights.copy()) , 0
        for i , item in enumerate(expected):
            if item != heights[i]:
                ans += 1 
        return ans