class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n  , ans , seen = len(fruits) , 0 , set()
        for i in range(n):
            exists = False
            for j in range(n):
                if fruits[i]<=baskets[j] and j not in seen:
                    exists = True
                    seen.add(j)
                    break
            if not exists:
                ans += 1
        return ans

