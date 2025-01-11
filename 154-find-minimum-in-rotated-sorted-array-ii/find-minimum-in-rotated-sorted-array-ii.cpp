class Solution {
public:
    int findMin(vector<int>& nums) {
         for(int i=0;i<nums.size();i++){
          for(int j=0;j<nums.size()-i;j--){
            if(nums[j]>nums[i]){ swap(nums[j],nums[i]);}}}
    return nums[0]; return 0;
    }
};