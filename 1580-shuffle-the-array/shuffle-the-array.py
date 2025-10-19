class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x, y = nums[:n], nums[n:]
        return [item for pair in zip(x, y) for item in pair]