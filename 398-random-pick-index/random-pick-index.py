import random
class Solution:
    def __init__(self, nums: List[int]):
        self.group = defaultdict(list)
        for i,item in enumerate(nums):
                self.group[item].append(i)
    def pick(self, target: int) -> int:
        return random.choice(self.group[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)