class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
         reverse(digits.begin(), digits.end());
       int size=digits.size();

       bool all9=true;
       for(int i=0;i<size;i++){if(digits[i]!=9){all9=false;}}


       if(all9){digits.push_back(0);digits[size]=1;
       for(int i=0;i<size;i++){digits[i]=0;}}

      else{digits[0]=digits[0]+1;
      for(int i=0;i<size;i++){
        if(digits[i]==10){digits[i+1]=digits[i+1]+1;
        digits[i]=0;}
      } }
      reverse(digits.begin(),digits.end());
        return digits;
    }
};