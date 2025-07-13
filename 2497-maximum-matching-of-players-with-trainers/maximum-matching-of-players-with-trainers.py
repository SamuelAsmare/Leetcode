class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m , n = len(players) , len(trainers)
        p , t , ans  = 0 , 0 , 0
        while p<m and t<n:
            if players[p] <= trainers[t]:
                ans += 1
                t+=1
                p += 1
            elif players[p]>trainers[t]:
                t+=1
        return ans

