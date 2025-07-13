class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p  , ans  = 0 , 0 
        for t in range(len(trainers)):
            if trainers[t] >= players[p]:
                ans+=1
                p+=1
                if p == len(players):
                    break
            else:
                continue

        return ans

