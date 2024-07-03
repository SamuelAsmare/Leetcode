class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        # Convert the integer to a string
        str_x = str(x)
        
        # Check if the string reads the same backward as forward
        return str_x == str_x[::-1]

        