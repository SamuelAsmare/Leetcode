class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minimum,counter,se=float('inf'),0,set()
        for i, sam in enumerate(nums):
            if (sam not in se):
                se.add(sam)
                counter+=1
            if(minimum>sam):
                minimum=sam
        if(k>minimum):
            return -1
        if(k in se):
            return counter-1
        return counter