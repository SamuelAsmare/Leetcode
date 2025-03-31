class Solution:
    def countTriples(self, n: int) -> int:
        myset = set()
        arr = []

        if n<3:
            return 0
        ans  =  0

        for i in range(1, n+1):
            c = i*i

            for num in arr:
                if c-num in myset:
                    ans+=1
            myset.add(c)
            arr.append(c)
        return ans