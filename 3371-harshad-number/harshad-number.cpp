class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
         int temp=x; int sum=0;
        while(x>0 ){
        sum=sum+x%10; x=x/10;}
       if(temp%sum!=0){return -1;}
       return sum;
    }
};