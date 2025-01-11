class Solution {
public:
    int findNonMinOrMax(vector<int>& nums) {
        if(nums.size()>100||nums.size()<1){ return -1;}
      if(nums.size()==2||nums.size()==1){return -1;}
      for(int i=0;i<nums.size();i++){
       for(int j=0;j<nums.size();j++){
       if(nums[i]>nums[j]){
      int temp=nums[i];nums[i]=nums[j]; nums[j]=temp; }} }
      return nums[1]; 
    }
};