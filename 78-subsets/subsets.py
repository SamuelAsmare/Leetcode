class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return list([list(sam) for n in range(len(nums)+1) for sam in combinations(nums,n)])
        