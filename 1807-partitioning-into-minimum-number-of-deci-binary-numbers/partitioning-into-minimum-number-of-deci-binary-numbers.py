class Solution:
    def minPartitions(self, n: str) -> int:
        ans = "1"
        for item in n:
            ans = max(ans , item)
        return int(ans)
