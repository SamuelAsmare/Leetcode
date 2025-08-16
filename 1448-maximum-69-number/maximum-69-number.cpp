class Solution {
public:
    int maximum69Number (int num) {
        vector<int> sam; int sum=0;
      while(num>0){
        sam.push_back(num%10);
        num=num/10;} 
        reverse(sam.begin(),sam.end());
      

        for(int i=0; i<sam.size(); i++){
            if(sam[i]==6){sam[i]=9; break;} 

        }
         for(int i=0;i<sam.size();i++){
           sum=sum+(sam[i]*pow(10,sam.size()-i-1));
        }return sum;   
    }
};