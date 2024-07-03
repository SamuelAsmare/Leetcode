class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        if negative:
            x = -x
        
        # Reverse the integer by converting to string, reversing, and converting back to int
        reversed_x = int(str(x)[::-1])
        
        # If the reversed integer is out of the 32-bit signed integer range, return 0
        if reversed_x > 2**31 - 1:
            return 0
        
        # If the original number was negative, return the negative of the reversed number
        return -reversed_x if negative else reversed_x
        