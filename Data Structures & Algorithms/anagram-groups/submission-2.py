class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            results[sorted_s].append(s)
        return list(results.values())

            

        