class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_mod = re.findall("[A-Za-z0-9]", s)
        for i in range(len(s_mod)):
            if s_mod[i].lower() == s_mod[- 1 - i].lower():
                continue
            else:
                return False
        # s_mod = [item.lower() if isinstance(item, str) else item for item in s_mod]
        # return s_mod == s_mod[::-1]
        return True
        