class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Step 1: Handle special cases: negative numbers can't be palindromes
        if x < 0:
            return False

        # Step 2: Keep the original value of x because we'll modify x in the loop
        original = x 

        # Step 3: This will hold the reversed version of x
        reversed_num = 0 
        while x > 0:
            # Get the last digit of x (e.g., if x = 123, then x % 10 = 3).
            last_digit = x % 10

            # Add the last digit to reversed_num (e.g., reversed_num = 0 * 10 + 3 = 3).
            reversed_num = reversed_num * 10 + last_digit

            # Remove the last digit from x (e.g., x = 123 // 10 = 12).
            x //= 10

        # Step 4: Compare the reversed number with the original
        return original == reversed_num

