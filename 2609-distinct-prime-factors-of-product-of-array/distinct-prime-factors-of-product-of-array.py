class Solution:
    def distinctPrimeFactors(self, nums):
        primes = set()
        def factorize(n):
            while n % 2 == 0:
                primes.add(2)
                n //= 2
            for i in range(3, int(sqrt(n)) + 1, 2):
                while n % i == 0:
                    primes.add(i)
                    n //= i
            if n > 2:
                primes.add(n)
        for num in nums:
            factorize(num)
        return len(primes)
