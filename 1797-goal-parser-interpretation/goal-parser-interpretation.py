class Solution:
    def interpret(self, command: str) -> str:
        string=""
        for i in range(len(command)):
            if (command[i]=='G'):
                string+='G'
            elif(command[i]=='(' and command[i+1]==')'):
                string+='o'
                i+=1
            elif (command[i]=='(' and command[i+1]=='a'):
                string+="al"
                i+=3
        return string
