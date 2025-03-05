class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        lowercase=False
        uppercase=False
        digit=False
        specialcharacter=False
        if(len(password)<8):
            return False
        for i in range (len(password)-1):
            if(password[i]==password[i+1]):
                return False
        for i in range(len (password)):
            askii=ord(password[i])
            if(askii>96 and askii<123):
                lowercase=True
            elif(askii>64 and askii<91):
                uppercase=True
            elif(askii>47 and askii<58):
                digit=True
            else:
                specialcharacter=True
        return digit and specialcharacter and lowercase and uppercase
