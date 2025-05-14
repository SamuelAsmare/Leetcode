class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res  , n = [pref[0]] , len(pref)
        for i in range(1,n):
            val = pref[i] ^ pref[i-1]
            res.append(val)
        return res
        