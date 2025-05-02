class Solution:
    def checkvowels(self,word):
        noother=True
        for i in range(len(word)):
            if(word[i]!='a' and word[i]!='e' and word[i]!='i' and word[i]!='o' and word[i]!='u' ):
                noother=False
        return noother
    def countVowelSubstrings(self, word: str) -> int:
        count=0
        subarr=[word[i:j+1] for i in range (len(word)) for j in range(i,len(word))]
        for i in range(len(subarr)):
            if(self.checkvowels(subarr[i]) and (('a'in subarr[i] )and ('e' in subarr[i]) and ('i' in subarr[i]) and ('o' in subarr[i]) and ('u' in subarr[i]))):
                count+=1
        return count