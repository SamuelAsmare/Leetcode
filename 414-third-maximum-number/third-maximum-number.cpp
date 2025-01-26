class Solution {
public:
    int thirdMax(vector<int>& nums) {
    sort(nums.begin(), nums.end());
     auto sam=unique(nums.begin(), nums.end());
     nums.erase(sam, nums.end());
     if(nums.size()<=2){return nums[nums.size()-1];}
     return nums[nums.size()-3];
    }
};