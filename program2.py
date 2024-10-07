class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to map Roman numerals to their respective values
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate over the characters of the Roman numeral from right to left
        for char in reversed(s):
            # Get the integer value of the current Roman numeral character
            current_value = roman_map[char]
            
            # If the current value is less than the previous value, we subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            # Update the previous value to the current one for the next iteration
            prev_value = current_value
        
        return total



