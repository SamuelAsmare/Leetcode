from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()  
        q = deque()
        for item in reversed(deck):
            if q:
                q.appendleft(q.pop()) 
            q.appendleft(item)
        return list(q)
