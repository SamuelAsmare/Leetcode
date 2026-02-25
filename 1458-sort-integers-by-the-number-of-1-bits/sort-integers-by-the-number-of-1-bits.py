class Solution:
    def count(self , num):
        ans = 0
        while num > 0:
            if num & 1:
                ans += 1
            num >>= 1
        return ans
    def sortByBits(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            ones = self.count(arr[i])
            arr[i] = [arr[i] , ones]
        arr.sort(key = lambda x : (x[1] , x[0]))
        return [item[0] for item in arr]