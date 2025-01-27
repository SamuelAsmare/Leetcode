class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        minimum=len(nums)//3
        majority=[]
        frequencyarray=Counter(nums)
        for i in frequencyarray:
            if frequencyarray[i]>minimum:
                majority.append(i)

        return majority
        