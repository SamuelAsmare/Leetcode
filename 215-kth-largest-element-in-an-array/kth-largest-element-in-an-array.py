class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapify(nums, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)

        def call(nums):
            n=len(nums)
            for i in range(n//2 - 1 , -1 , -1):
                heapify(nums,n,i)
        call(nums)  #  I have finished max-heap construction
        counter=1
        temp=nums[0]
        nums[0]=nums[-1]
        nums.pop()
        while(counter<k):
            n=len(nums)
            heapify(nums,n,0)
            temp,nums[0]=nums[0],nums[-1]
            nums.pop()
            counter+=1
        return temp

            



