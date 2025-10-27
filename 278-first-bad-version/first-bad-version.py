# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low , high = 1, n
        if isBadVersion(low):
            return low
        if isBadVersion(high) and not isBadVersion(high-1):
            return high
        while low < high:
            mid = (low + high)//2
            print(mid)
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    high = mid
                else:
                    return mid
            else:
                low = mid

# 1,2,3,4,5