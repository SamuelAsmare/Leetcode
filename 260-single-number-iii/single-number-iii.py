class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        fre=Counter(nums)
        arr=[]
        for i in range (len(nums)):
            if fre[nums[i]]==1:
                arr.append(nums[i])
        return arr