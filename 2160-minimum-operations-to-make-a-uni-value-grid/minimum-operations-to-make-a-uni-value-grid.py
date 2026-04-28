class Solution:
    def minOperations(self, grid, x):
        arr = []
        ans = 0
        for row in grid:
            for num in row:
                arr.append(num)
        arr.sort()
        length = len(arr)
        median = arr[length // 2]
        for number in arr:
            if number % x != median % x:
                return -1
            ans += abs(median - number) // x
        return ans