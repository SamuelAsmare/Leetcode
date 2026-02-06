class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        i , max_size , n =  0 , 1 , len(nums)
        for j in range(1 , n):
            while nums[j] > nums[i] * k and i < j:
                i += 1
            max_size = max(max_size , j - i + 1)
        return n - max_size
            
