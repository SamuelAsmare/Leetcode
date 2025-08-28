class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        fre , ans  = Counter(nums) , []
        for item in fre:
            if fre[item] == 1 and item+1 not in fre and item - 1 not in fre:
                ans.append(item)
        return ans