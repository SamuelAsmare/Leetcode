class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0 , 0]
        for item in moves:
            if item == "U":
                pos[0] -= 1
            elif item == "D":
                pos[0]  += 1
            elif item == "L":
                pos[1] -= 1
            else:
                pos[1] += 1
        return pos == [0 , 0]
#  [2 , 0]
