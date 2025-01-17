class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int>ans; int counter=0;
        while(counter<=1){
            for(int i=0;i<nums.size();i++){
                ans.push_back(nums[i]);  }counter ++;  } 
   return ans; }
};