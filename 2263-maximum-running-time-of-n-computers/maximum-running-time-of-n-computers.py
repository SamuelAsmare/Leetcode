class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
            batteries.sort()
            extra = sum(batteries[:-n])
            live = len(batteries) - n
            for i in range(live,live + n - 1):
                if extra < (i-live+1)*(batteries[i+1] - batteries[i]):
                    return batteries[i] + extra//(i - live + 1)
                extra -= (batteries[i+1] - batteries[i])*(i-live+1)
            return batteries[-1] + extra//n
            