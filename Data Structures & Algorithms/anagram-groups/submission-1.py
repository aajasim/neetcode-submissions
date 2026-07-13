class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for i in range(len(s)):
                val = ord(s[i]) - ord("a")
                counter[val] += 1
            res[tuple(counter)].append(s)
        return list(res.values())


