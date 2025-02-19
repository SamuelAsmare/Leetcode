class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        fre=Counter(nums)
        result=0
        new=list(set(nums))
        for i in range(len(new)):
            if(fre[new[i]]==2):
                result=result^new[i]
        return result
