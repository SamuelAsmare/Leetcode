class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
      vector<int> sam;
     if(val>100||val<0){return -1;}
     if(nums.size()>100||nums.size()<0){return -1;}
     bool found=true;
     for(int i=0; i<nums.size(); i++){
      if(nums[i]<0||nums[i]>50){return -1;}
        
        if(nums[i]!=val){
            sam.push_back(nums[i]);}     
         }  nums.clear();
     for(int i=0; i<sam.size(); i++){
      nums.push_back(sam[i]);}
           return nums.size();     
    }
};