class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> result;
    for(int i=0;i<n;i++){
      result.push_back(nums[i]);
      result.push_back(nums[i+n]);
    }
    nums.clear();
    for(int i=0;i<result.size();i++){
      nums.push_back(result[i]);
    }return nums;
    }
};