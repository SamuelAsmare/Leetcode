class Solution:
    def __init__(self):
        self.memo = dict()
    def fib(self, n: int) -> int:
        if n == 1 or n==0:
            return n
        if n not in self.memo:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]
    