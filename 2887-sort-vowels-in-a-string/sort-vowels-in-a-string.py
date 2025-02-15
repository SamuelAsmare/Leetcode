class Solution:
    def sortVowels(self, s: str) -> str:
        #first conver the string to character array(list)
        new=list(s)
        #declare a temporary list to store vowels
        vowels=[]
        for i in range(len(new)) :
            if (new[i].lower()=='a' or new[i].lower()=='e' or new[i].lower()=='i'or new[i].lower()=='o'or new[i].lower()=='u'):
                vowels.append(new[i])
                new[i]='*'
        vowels.sort()
        for i in range (len(new)):
            if(new[i]=='*'):
                new[i]=vowels[0]
                vowels.remove(vowels[0])
        s="".join(new)
        return s
