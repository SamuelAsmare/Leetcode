class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if all([digits[i]==9 for i in range(n)]):
            digits = [0]*(n + 1)
            digits[0] = 1
            return digits
        digits[-1] += 1
        for i in range(n-1 , -1 , -1):
            print(digits)
            if digits[i] > 9:
                digits[i] = digits[i]%10
                digits[i-1] += 1
            else:
                break
        return digits
        

