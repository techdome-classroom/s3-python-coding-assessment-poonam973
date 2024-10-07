class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to hold matching pairs
        matching_brackets = {')': '(', '}': '{', ']': '['}
        
        # Stack to keep track of opening brackets
        stack = []
        
        # Iterate through each character in the string
        for char in s:
            if char in matching_brackets:
                # Pop the topmost element from the stack if not empty, else assign '#'
                top_element = stack.pop() if stack else '#'
                
                # If the top element doesn't match the corresponding opening bracket, return False
                if matching_brackets[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it to the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched correctly, return True
        # Otherwise, return False
        return not stack







    



  

