class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x-z) > abs(y-z):return 2
        if abs(x-z) < abs(y-z):return 1
        return 0