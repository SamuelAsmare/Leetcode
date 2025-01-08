class Solution {
public:
    bool isPowerOfThree(int n) {
int sum=0;
        if(n<0){return 0;}
        if(n==1){return true;}
        if(n==0){return 0;}

        while(n>0){
            sum=sum+(n%3);
            n=n/3;          
             
        }
        
        if(sum==1){return true;}
        
         else{   return false;}   
    
    }
};