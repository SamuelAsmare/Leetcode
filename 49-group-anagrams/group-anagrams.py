class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for item in strs:
            key  = "".join(sorted(item))
            group[key].append(item)
        return list(group.values())