class Solution:
    def countValidSelections(self, a: List[int]) -> int:
        def ok(i, d):
            b = a[:]
            n = len(b)
            while 0 <= i < n:
                if b[i] == 0:
                    i += d
                else:
                    b[i] -= 1
                    d *= -1
                    i += d
            return all(x == 0 for x in b)
        ans = 0
        for i, x in enumerate(a):
            if x == 0:
                ans += ok(i, 1) + ok(i, -1)
        return ans
