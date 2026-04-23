class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        index = defaultdict(list)
        for i , item in enumerate(arr):
            index[item].append(i)
        for val in index:
            prefix = []
            for item in index[val]:
                if prefix:
                    prefix.append(prefix[-1] + item)
                else:
                    prefix.append(item) 
            total , n  = prefix[-1] , len(prefix)
            for i , item in enumerate(index[val]):
                arr[item] = 0
                if i > 0:
                    arr[item] += i * item - prefix[i - 1]
                if i < n - 1:
                    rem = total - prefix[i]
                    arr[item] += rem - (n - i - 1)*(item)
        return arr
                    
                

