class Solution:
    def prime_set(self , num):
        primes = {2,3,5,7,11,13,17,19}
        set_bits = 0
        while num > 0:
            if num & 1:
                set_bits += 1
            num >>= 1
        return set_bits in primes
            
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for num in range(left ,  right + 1):
            if self.prime_set(num):
                ans += 1
        return ans