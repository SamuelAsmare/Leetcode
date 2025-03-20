class Solution(object):
    def checkDistances(self, s, distance):
        exist=0
        for i in range(len(s)):
            if(s[i]!=" "):
                temp=s[i]
                s=s[:i]+ " " + s[i+1:]
                asciiindex=ord(temp)-97
                index=s.index(temp)
                s=s[:index]+" "+s[index+1:]
                if(index-i-1!= distance[asciiindex]):
                    return False
            else:
                continue
        return True


        