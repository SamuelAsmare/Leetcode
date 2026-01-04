class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        ans = 0
        for n in nums:
            p = round(n ** (1/3))
            if p * p * p == n and is_prime(p):
                ans += 1 + p + p*p + n
                continue
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    j = n // i
                    if i != j and is_prime(i) and is_prime(j):
                        ans += 1 + i + j + n
                    break
        return ans
