class Solution {
public:
    int findGCD(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int large=nums[nums.size()-1];
        int small = nums[0]; vector<int> sam;
        for(int i=1;i<=small;i++){
            if(small%i==0 && large%i==0){
                sam.push_back(i);
            }     } return sam[sam.size()-1];
    }
};