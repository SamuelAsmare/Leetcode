class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right=len(numbers)-1
        for left in range(len(numbers)):
            while(numbers[right]+numbers[left]>target):
                right -=1
            if(numbers[right]+numbers[left]==target):
                return [left+1,right+1]

        return []