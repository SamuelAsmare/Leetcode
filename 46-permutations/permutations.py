class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=list(permutations(nums))
        return result