class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        vector<int> sam; int size=nums.size();
         for(int i=0; i<size; i++){
          if(nums[i]%2==0){sam.push_back(nums[i]);}}
          for(int i=0; i<size; i++){
          if(nums[i]%2!=0){sam.push_back(nums[i]);}}
          return sam;
    }
};