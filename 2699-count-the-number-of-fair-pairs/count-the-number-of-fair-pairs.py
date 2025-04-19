class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        count = 0
      

        for i in range(len(nums)):
            l = lower-nums[i]
            u = upper - nums[i]
            left, right = i+1, len(nums)-1
            ansu = float("inf")
            while right>=left:
                mid = (right+left)//2

                if nums[mid]<= u:
                    ansu = mid
                    left= mid+1
                else:
                    right = mid-1
            if ansu == float("inf"):
                return count
            left, right = i+1, len(nums)-1
            ansl = float("inf")
            
            while right>= left:
                mid = (right+left)//2

                if nums[mid] >= l:
                    ansl = mid
                    right=mid-1
                else:
                    left = mid+1
            if ansl == float("inf"):
                continue
            count+=ansu-ansl+1
        return count






