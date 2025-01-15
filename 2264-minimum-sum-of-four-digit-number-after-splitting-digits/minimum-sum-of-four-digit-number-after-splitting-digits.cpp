class Solution {
public:
    int minimumSum(int num) {
       vector<int> sam;vector<int> candidates;
      while(num>0){
     sam.push_back(num%10); num=num/10;}
      sort(sam.begin(), sam.end());
      candidates.push_back(sam[0]);
      sam.erase(sam.begin()+0);
      candidates.push_back(sam[2]);
      sam.erase(sam.begin()+2); int num1=10*sam[0]+sam[1];
       int num2=10*candidates[0]+candidates[1];
      return num1+num2;    
    }
};