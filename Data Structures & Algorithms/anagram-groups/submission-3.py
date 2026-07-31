class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                counter[idx] += 1
            results[tuple(counter)].append(s)
        return list(results.values())