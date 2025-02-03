class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
       maxsize=max(len(bin(start)),len(bin(goal)))
       count=0
       sbin=bin(start)[2:].zfill(maxsize)
       gbin=bin(goal)[2:].zfill(maxsize)
       for i in range(len(sbin)):
        if gbin[i]!=sbin[i]:
            count+=1
       return count
        