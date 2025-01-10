class Solution {
public:
    int mySqrt(int x) {
        vector<int> sam; if(x<0){ return-1;}
    for(unsigned i=0;i*i<=x;i++){
      if(i*i>INT_MAX){return -1;}
      sam.push_back(i);  }
      return sam[sam.size()-1];  
        
    }
};