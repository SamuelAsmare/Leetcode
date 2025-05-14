class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set([sam for sam in permutations(nums)]))