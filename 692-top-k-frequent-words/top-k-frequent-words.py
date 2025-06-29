class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        fre  , ans = Counter(words) , []
        key_value_pairs = fre.items()
        result = sorted(key_value_pairs , key = lambda x:(-x[1],x[0]))
        return [value[0] for value in result][:k]