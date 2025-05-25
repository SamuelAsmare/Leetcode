class Solution:
    def canWinNim(self, n: int) -> bool:
        myturn = n%4
        return myturn != 0