class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans  = set()
        for word in dictionary: # 100
            for val , query in enumerate(queries): # 100
                if len(word) != len(query):
                    continue
                edits = 0
                for i in range(len(word)):
                    if word[i] != query[i]:
                        edits += 1
                        if edits > 2:
                            break
                else:
                    ans.add(val)
        return [queries[i] for i in range(len(queries)) if i in ans]
        


        
