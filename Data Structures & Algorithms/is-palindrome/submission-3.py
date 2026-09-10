class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_corr = [char.lower() for char in s if char.isalnum()]
        return s_corr == s_corr[::-1]