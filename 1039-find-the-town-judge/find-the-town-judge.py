class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dic=defaultdict(set)
        fir,sec=set(),set()
        for i in range(len(trust)):
            fir.add(trust[i][0])
            sec.add(trust[i][1])
            dic[trust[i][1]].add(trust[i][0])
            trust[i].remove(trust[i][0])
        for i in range(1,n+1):
            if len(dic[i])==n-1 and i not in fir:
                return i
        return -1 