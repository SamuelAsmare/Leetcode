class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        fre1 , fre2 = Counter(word1) , Counter(word2)
        print(fre1.values() ,fre2.values() ,  fre1.keys() , fre2.keys())
        return (
                sorted(fre1.values()) == sorted(fre2.values())
                and
                sorted(fre1.keys()) == sorted(fre2.keys())            )

