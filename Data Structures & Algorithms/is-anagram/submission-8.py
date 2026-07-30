class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for i in range(len(s)):
            index_s = ord(s[i]) - ord("a")
            index_t = ord(t[i]) - ord("a")
            counter[index_s] += 1
            counter[index_t] -= 1
        for i in range(len(counter)):
            if counter[i] != 0:
                return False
        return True
        