class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        values  = defaultdict(int)
        for i , item in enumerate(bills):
            if item == 5:
                values[5]+=1
            elif item == 10:
                if values[5]==0:
                    return False
                else:
                    values[10]+=1
                    values[5]-=1
            elif item==20:
                if values[5]==0:
                    return False
                elif values[10]==0:
                    if values[5]<3:
                        return False 
                    else:
                        values[5]-=3                   
                else:
                    values[10]-=1
                    values[5]-=1            
        return True


