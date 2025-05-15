class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n , maxpro = len(words) , 0
        binary = [0] * n
        # am creating an array for putting the binart values of each word
        for i , word in enumerate(words): # for putting the value of each character
            mybitmask = 0
            for char in word: 
                index = ord(char) - 97 
                mybitmask = mybitmask | 1 << index # left shift
            binary[i] = mybitmask
        for i in range(n):
            for j in range(i+1,n):
                if not binary[ i ] & binary[ j ]: # if they have no intersection....
                    maxpro = max (maxpro, len(words[ i ]) * len(words[ j ]))
        return maxpro


