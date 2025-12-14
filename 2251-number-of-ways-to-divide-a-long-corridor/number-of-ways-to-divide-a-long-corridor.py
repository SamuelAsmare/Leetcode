class Solution:
    def numberOfWays(self, C: str) -> int:
        mod =  10**9 + 7
        ans , seats = 1 ,  []
        for i,item in enumerate(C) :
            if item == "S":
                seats.append(i)
        if len(seats) < 2 or len(seats) & 1:
            return 0
        for i in range(1,len(seats)-1,2):
            ans = (ans*(seats[i+1] - seats[i]))%mod
        return ans