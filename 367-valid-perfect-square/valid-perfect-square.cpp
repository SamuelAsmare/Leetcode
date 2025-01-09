class Solution {
public:
    bool isPerfectSquare(int num) {
       bool isperfect = true;
       if(int(sqrt(num)) *int( sqrt(num) )!= num){
       isperfect=false;   }return isperfect;
    }
};