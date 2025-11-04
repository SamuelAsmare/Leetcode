class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freq = Counter(sub)
            sorted_items = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
            top_x = set([num for num, _ in sorted_items[:x]])
            total = sum(num for num in sub if num in top_x)
            res.append(total)
        return res
