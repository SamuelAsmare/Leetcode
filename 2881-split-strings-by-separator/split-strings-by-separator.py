class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans=[]
        for word in words:
                    ans.extend(word.split(separator))
        ans=[x for x in ans if x!='']
        return ans