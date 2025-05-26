class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic , s , dic2 = defaultdict(set) , s.split(" ") , defaultdict(set)
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            dic[pattern[i]].add(s[i])
            dic2[s[i]].add(pattern[i])
            if len(dic[pattern[i]]) >= 2 or len(dic2[s[i]])>=2:
                return False
        print(dic,dic2)
        return True