class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the result integer
        result = 0
        
        # Iterate through the string of Roman numerals
        for i in range(len(s)):
            # If the current Roman numeral is less than the next one, subtract its value
            if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                result -= roman_dict[s[i]]
            # Otherwise, add its value
            else:
                result += roman_dict[s[i]]
        
        return result
        