class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        if(len(nums)==1 and nums[0]==target):
            return 0
        while(right>left):
            if(nums[left]==target):
                return left
            elif(nums[right]==target):
                return right
            mid=(left+right)//2
            if(nums[mid]==target):
                return mid
            if(nums[mid]>target):
                right=mid-1
            if(nums[mid]<target):
                left=mid+1
        return -1
