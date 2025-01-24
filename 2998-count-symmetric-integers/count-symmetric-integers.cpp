class Solution {
public:
bool symmetric(int n) {
    vector<int> sam; int sum1=0,sum2=0 ;
    while(n>0){sam.push_back(n%10); 
         sum1=sum1+n%10; n/=10;}
    if(sam.size()%2!=0){return false;}
     for(int i=0;i<sam.size()/2;i++){sum2=sum2+sam[i]; }
           return sum1-sum2==sum2;
    
}
int countSymmetricIntegers(int low, int high) {
    int counter=0;
       for(int i=low;i<=high;i++){
           if(symmetric(i)){counter++;}
    } return counter;
    }

};