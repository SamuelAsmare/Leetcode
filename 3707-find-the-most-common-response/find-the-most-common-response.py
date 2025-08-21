class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counter = Counter()
        for day in responses:
            unique_responses = set(day)  
            for resp in unique_responses:
                counter[resp] += 1   
        max_freq = max(counter.values())
        candidates = [resp for resp, freq in counter.items() if freq == max_freq]
        return min(candidates)
