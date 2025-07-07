class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen , ans = set () , []
        for item in nums:
            if item in seen:
                ans.append(item)
            else:
                seen.add(item)
        return ans
