class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if (digits==""):
            return []
        dic= {
            "2" :  ["a","b","c"],
            "3" :  ["d","e","f"],
           "4" :   ["g","h","i"],
            "5" :  ["j","k","l"],
            "6" :  ["m","n","o"],
            "7" :  ["p","q","r","s"],
            "8" :  ["t","u","v"],
            "9" :  ["w","x","y","z"]
        }
        candidates=[]
        for j in digits:
            candidates.append(dic[j])
        combinations = itertools.product(*candidates)
        res = ["".join(map(str,eachtuple)) for eachtuple in combinations]
        return res