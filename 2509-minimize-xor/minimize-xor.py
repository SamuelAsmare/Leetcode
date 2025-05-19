class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c = bin(num2).count('1')
        x = 0
        for i in range(31, -1, -1):
            if c > 0 and (num1 >> i) & 1:
                x |= 1 << i
                c -= 1
        for i in range(32):
            if c > 0  and not (x >> i) & 1:
                x |= 1 << i
                c -= 1
        return x