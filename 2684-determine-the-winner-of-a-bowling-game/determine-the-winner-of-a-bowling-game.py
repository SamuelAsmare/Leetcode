class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n  , p1 , p2 = len(player1) , 0 , 0
        for i in range(n):
            # calculate player 1
            if i >= 2 and  player1[i-2] == 10: # 10 + 
                p1 += 2*player1[i]
            elif i >= 1 and player1[i-1] == 10:
                p1 += 2*player1[i]
            else:
                p1 += player1[i]
            # calculate player 2
            if i >= 2 and player2[i-2] == 10:
                p2 += 2*player2[i]
            elif i >= 1 and player2[i-1] == 10:
                p2 += 2*player2[i]
            else:
                p2 += player2[i]
        print(p1,p2)
        if p1 > p2:
            return 1
        if p1 < p2:
            return 2
        return 0
        

                

