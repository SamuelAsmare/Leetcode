from typing import List
class Solution:
    def subsets(self , nums: List[int]) -> List[List[int]]:

        n  , result = len(nums) , []

        for mask in range(1 << n):

            subset = []

            for j in range(n):
                
                if mask & (1 << j):

                    subset.append(nums[j])
                    
            result.append(subset)
        
        return result

