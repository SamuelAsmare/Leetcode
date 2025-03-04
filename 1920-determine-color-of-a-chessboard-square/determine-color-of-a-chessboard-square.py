class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        arr=["a","b","c","d","e","f","g","h"]
        if(coordinates[1].isdigit()):
             if(int(coordinates[1])%2==0  and  arr.index(coordinates[0])%2==0):
                     return True
             if(int(coordinates[1])%2!=0  and arr.index(coordinates[0])%2!=0):
                     return True
       

        return False
        