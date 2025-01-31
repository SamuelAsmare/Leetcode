class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        sam=[]
        for i in range(len(nums)):
            sam.insert(index[i],nums[i])
        return sam
        