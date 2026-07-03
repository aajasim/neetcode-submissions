class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted(list(s))
        list_t = sorted(list(t))

        if len(list_s) != len(list_t):
            return False
        else:
            for i in range(len(list_s)):
                    if list_s[i] != list_t[i]:
                        return False
        return True
        