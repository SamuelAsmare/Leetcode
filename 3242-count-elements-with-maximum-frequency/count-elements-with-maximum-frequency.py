class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        fre=Counter(nums)
        maxfre=0
        counter=0
        for i in nums:
            if fre[i]>maxfre:
                maxfre=fre[i]
        for i in nums:
            if fre[i]==maxfre:
                counter+=1
        return counter
            