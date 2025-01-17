class Solution {
public:
bool self(int number){
    vector<int>temp; int n=number;
    while(n>0)
    {if(n%10==0){return false;}
      temp.push_back(n%10);
      n=n/10; }   
      for(int i=0; i<temp.size(); i++){
         if(number%temp[i]!=0){return false;            
         } }return true;}
    vector<int> selfDividingNumbers(int left, int right) {
         vector<int> result;
        for(int i=left; i<=right; i++){
            if(self(i)){result.push_back(i);}
        }return result;
    }
};