class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> leftsum,rightsum,diff; 
          for(int i=0; i<nums.size();i++){
            int sum1=0;
           for(int j=0; j<i;j++){
           sum1=sum1+nums[j]; }leftsum.push_back(sum1);
          }  
          for(int i=nums.size()-1; i>=0;i--){
            int sum2=0;
           for(int j=nums.size()-1; j>i;j--){
           sum2=sum2+nums[j]; }rightsum.push_back(sum2);
          } reverse(rightsum.begin(), rightsum.end());
          for(int i=0;i<nums.size();i++){
            diff.push_back(abs(leftsum[i]-rightsum[i]));
          }return diff;
    }
};