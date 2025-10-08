class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool: 
        # arr = [1,2,3,4,0,0,1,2,3,4], k = 5
        freq = [0 for i in range (k)]  
        for item in arr:
            freq[item%k] += 1
        for item in range(1,k):
            if k-item == item and freq[item] & 1 :
                return False
            if freq[item] != freq[k-item]:
                return False
        return True
       