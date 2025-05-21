class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for eachword in strs:
            mykey = "".join(sorted(eachword))
            dic[mykey].append(eachword)
        return list(dic.values())
