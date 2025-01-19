class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        vector<int>sam;int sum=0;
        for(int i=0;i<nums.size();i++){
          bool found=true;
          for(int j=0;j<nums.size();j++){
            if(i==j){continue;}
            if(nums[i]==nums[j]){found=false;}
          }
          if(found){sam.push_back(nums[i]);} } 
          for(int i= 0;i<sam.size();i++){sum=sum+sam[i];}
          return sum;
    }
};