class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
       vector<int> sam;int size=nums.size();
       int sum =0;
       for(int i=0;i<size;i++){
         sum=sum+nums[i];sam.push_back(sum);
       }return sam;    
    }
};