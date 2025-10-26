class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]
        def build(arr):
            if len(arr)-1 == n:
                return arr
            else:
                curr = [1]
                for i in range(1,len(arr)):
                    curr.append(arr[i-1] + arr[i])
                curr.append(1)
                return build(curr)
        return  build([1])
