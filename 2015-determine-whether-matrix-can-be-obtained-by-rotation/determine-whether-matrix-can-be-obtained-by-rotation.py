
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        arr = mat
        for _ in range(4):
            arr = [list(col) for col in zip(*arr)][::-1]
            if arr == target:
                return True
        return False

