class Solution:
    def judgeCircle(self, moves: str) -> bool:
        fre = Counter(moves)
        return fre["L"] == fre["R"] and fre["U"] == fre["D"]
#  [2 , 0]
