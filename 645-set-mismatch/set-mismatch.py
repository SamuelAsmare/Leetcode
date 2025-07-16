class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        fre ,  n = Counter(nums) , len(nums)
        duplicate = miss = 0
        for i in range(1,n+1):
            if fre[i] == 2:
                duplicate = i
            if fre[i] == 0:
                miss = i
            if miss and duplicate:
                break
        return [duplicate , miss]