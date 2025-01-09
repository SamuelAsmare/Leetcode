class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
      vector<int> sam; int index=0;
     if(nums.size()>30000||nums.size()<1){return -1;}
     for(int i=0; i<nums.size(); i++){
      if(nums[i]<-100||nums[i]>100){return -1;}
        bool found=true;
        
        for(int j=1; j<=index; j++){

        if(nums[i]==sam[j-1]){found=false;}
        }

        if(found){ sam.push_back(nums[i]); index++; }
    }nums.clear();
     for(int i=0; i<sam.size(); i++){nums.push_back(sam[i]);}
     return nums.size();
    }
};