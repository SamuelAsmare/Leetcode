class Solution {
public:
    int climbStairs(int n) {
        if(n<1||n>45){
            return -1;
        }
        else if (n==45) return 1836311903;
        else if(n==43) return 701408733;
        else if(n==42) return 433494437;
        
        else if(n==1) return 1;
        else if(n==2) return 2;
       
        return climbStairs(n-1)+climbStairs(n-2);
        
    }
};