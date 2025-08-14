class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for right in range(2,len(num)):
            left = right-2
            if num[left]==num[left+1] and num[left+1]==num[right]:
                ans = max(num[left:right+1],ans)
        return ans
