class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        fre , ans = Counter(nums) , []
        return sorted(nums, key=lambda x:(fre[x],-x))
       