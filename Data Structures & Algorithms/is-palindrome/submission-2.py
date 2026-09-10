class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_corr = [char.lower() for char in s if char.isalnum()]
        for i in range(len(s_corr)//2):
            if s_corr[i] != s_corr[-1-i]:
                return False
        return True
        