class Solution:
    def minimumPushes(self, word: str) -> int:
        number = defaultdict(int)
        degree= defaultdict(int)
        fre = Counter(word)
        # if there are maximum of 8 elements return the length
        if len(fre)<=8:
            return len(word)
        # sort the fre
        fre = sorted(fre.items(), key=lambda x: -x[1])
        for i, (item,frequency) in enumerate(fre):
            current_number = (i+2)%8
            number[current_number]+=1
            degree[item] = number[current_number]
        ans = 0
        for item in word:
            ans += (degree[item])

        return ans

