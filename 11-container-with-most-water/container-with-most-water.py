class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans , left , right = 0 , 0 , len(height)-1
       
        while(left<right):
            width = min(height[left],height[right]) 

            area = (right-left)*width
            ans = max(ans,area)

            if height[left]<height[right]: # shrink
                left+=1
            else:
                right-=1
        return ans
            

