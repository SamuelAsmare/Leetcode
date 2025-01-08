class Solution {
public:
    bool isPowerOfFour(int n) {
        int sum=0;
        if(n<0){return 0;}
        if(n==1){return true;}
        if(n==0){return 0;}

        while(n>0){
            sum=sum+(n%4);
            n=n/4;          
             
        }
        
        if(sum==1){return true;}
        
         else{   return false;} 
    }
};