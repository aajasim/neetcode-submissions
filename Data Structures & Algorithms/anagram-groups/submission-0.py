class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []
        seen = []
        for i in range(len(strs)):
            check = [strs[i]]
            if strs[i] in seen:
                continue
            else:
                # seen.append(strs[i])
                for j in range(i+1, len(strs)):
                    if ''.join(sorted(strs[i]))==''.join(sorted(strs[j])):
                        check.append(strs[j])
                        seen.append(strs[j])
            group.append(check)
        return group

            
