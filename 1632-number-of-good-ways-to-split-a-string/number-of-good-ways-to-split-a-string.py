class Solution:
    def numSplits(self, s: str) -> int:
        ans , sleft , sright = 0 , Counter() , Counter(s)
        for item in s:
            sleft[item] += 1
            sright[item] -= 1
            if sright[item] == 0:
                del sright[item]
            if len(sleft) == len(sright):
                ans += 1
        return ans 
            
