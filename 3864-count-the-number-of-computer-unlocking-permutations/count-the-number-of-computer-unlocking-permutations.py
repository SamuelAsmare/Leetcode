class Solution:
    def countPermutations(self, C: List[int]) -> int:
        if min(C[1:]) <= C[0]: return 0
        MOD , ans = 10**9 + 7 , 1
        for i in range(2,len(C)):
            ans = (ans * i)%MOD
            print(ans)
        return ans
        #  6! = 6 ,5,4,3,2,