class Solution:
    def kthCharacter(self, k: int) -> str:
        counter ,string  = 1 , ['a']
        while counter<k:
            for i in range(len(string)):
                asciii = ord(string[i])+1
                if asciii >= 123:
                    asciii = asciii-26
                string.append(chr(asciii))
                counter+=1
        print(string)
        return string[k-1]