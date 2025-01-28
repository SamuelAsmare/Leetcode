class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int max=0; int temp=0; nums.push_back(nums[0]);
           for(int i=0; i<nums.size()-1; i++){
                temp=abs(nums[i]-nums[i+1]);
        if(temp>max) max=temp;  }
    return max;
    }
};