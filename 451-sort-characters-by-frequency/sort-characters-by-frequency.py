class Solution:
    def frequencySort(self, s: str) -> str:
        fre=Counter(s)
        sortedfre=sorted(fre.items(),key=lambda x: x[1],reverse=True)
        s=""
        for item,freq in sortedfre:
            s+=item*freq
        return s

