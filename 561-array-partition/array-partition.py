class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res  , n , temp = 0 , len(nums), []
        nums.sort()
        for i in range(n-2 , -1 , -2):
            res += nums[i]
            temp.append(nums[i])
        print(temp)
        return res
