class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if (len(word)==1):
            return True
        small=False
        capital=False

        if(word[0].upper()==word[0]):
            for i in range(1,len (word)):
                if(word[i].upper()==word[i]):
                    capital=True
                if(word[i].lower()==word[i]):
                    small=True
            if(capital and small):
                return False
        else:
            for i in range(len (word)):
                if(word[i].upper()==word[i]):
                    capital=True
                if(word[i].lower()==word[i]):
                    small=True
            if(capital and small):
                return False
        return True

 
            

         