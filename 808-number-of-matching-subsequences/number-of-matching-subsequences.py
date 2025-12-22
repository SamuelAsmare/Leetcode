class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices , ans = defaultdict(list) , 0
        for i , char in enumerate(s):
            indices[char].append(i)
        for i in range(len(words)):
            start_index = -1
            for item in words[i]:
                pos = bisect_right(indices[item],start_index)
                if pos >= len(indices[item]):
                    break
                else:
                    start_index = indices[item][pos]
            else:
                ans += 1
        return ans 



        