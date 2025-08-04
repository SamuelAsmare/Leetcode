class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans , n = [] , len(nums)
        for i , item in enumerate(nums):
            if item>0:
                ans.append(nums[(item+i)%n])
            else:
                print(item)
                ans.append(nums[(n-abs(item)+i)%n])   
        return ans