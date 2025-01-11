class Solution {
public:
    double minimumAverage(vector<int>& nums) {
        vector<double> sam; sort(nums.begin(), nums.end()); 
       for(int i=0;i<nums.size()/2;i++){
        for(int j=nums.size()-1-i;j>=nums.size()-1-i;j--){
          sam.push_back((nums[j]+nums[i])/2.0);     } }
          sort(sam.begin(), sam.end());
          return sam[0];
    }
};