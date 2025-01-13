class Solution {
public:
    int alternateDigitSum(int n) {
         vector<int> sam;
      while(n>0){
        sam.push_back(n%10);
        n=n/10;     }
        int sum=0;int temp;
        reverse(sam.begin(), sam.end());

        for(int i=0; i<sam.size(); i++) {
         if(i%2==0){temp=1;}
         else if(i%2!=0){temp=-1;}
         sum+=temp*sam[i];       }
         return sum; 
    }
};