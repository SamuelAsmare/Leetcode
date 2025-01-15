class Solution {

public:
int sumofbits(int n){
  int count=0; int sum=0;
  while(n>=0){ if(count==32){
  break;  } sum=sum+n%2;
    n=n/2;  count++; }
  return sum;
}
    vector<int> countBits(int n) {
        vector<int>sam; vector<int>final;
   for(int i=0;i<=n;i++)  {
    sam.push_back(sumofbits(i));
     } return sam;
    }
};