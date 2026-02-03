class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        c1 = c2 = c3 = False
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                if not c2:
                    c1 = True
                else:
                    for j in range(i, len(nums)-1):
                        if not nums[j] < nums[j+1]:
                            return False
                    c3 = True
                    break
            elif nums[i] > nums[i+1]:
                c2 = True
            else:
                return False
        return c1 and c2 and c3

           
#  [1,3,5,4,2,6]
#  

