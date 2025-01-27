class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        while(k>0):
            nums.insert(0,nums.pop(size-1))
            k=k-1
        
        