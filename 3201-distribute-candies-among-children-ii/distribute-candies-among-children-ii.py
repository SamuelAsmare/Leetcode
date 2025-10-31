from math import comb
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0
        answer = comb(n + 2, 2) # stars and bars
        if n > limit:
            answer -= 3 * comb(n - limit + 1, 2) # n-(limit+1) + 2
        if n - 2 >= 2 * limit:
            answer += 3 * comb(n - 2 * limit, 2)  # n-2(limit+1) + 2    
        return answer
