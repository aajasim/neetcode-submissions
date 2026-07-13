class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = [0] * 26
        for i in range(len(s)):
            num = ord(s[i]) - ord("a")
            lookup[num] += 1
        for j in range(len(t)):
            num = ord(t[j]) - ord("a")
            lookup[num] -= 1
        if any(lookup) != 0:
            return False
        else:
            return True