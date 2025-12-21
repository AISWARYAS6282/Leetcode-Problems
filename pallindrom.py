class Solution(object):
    def isPalindrome(self, x):
       # Negative numbers and non-zero numbers ending in 0 are not palindromes
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
            
        reversed_half = 0
        # Build the reverse of the second half
        while x > reversed_half:
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10
            
        # For even digits, x == reversed_half
        # For odd digits, we discard the middle digit via reversed_half // 10
        return x == reversed_half or x == reversed_half // 10