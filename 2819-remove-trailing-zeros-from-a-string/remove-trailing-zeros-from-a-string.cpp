class Solution {
public:
    string removeTrailingZeros(string num) {
      for(int i=num.length()-1;i>=0;i--){
           if(num[i]!='0'){return num;}
           num.erase(i,1);/* i=index of an element and 1 is the number of 
           characters to be removed from the string*/
        }return num;
    }
};