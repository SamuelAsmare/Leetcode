class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count =0; vector<int>sam;
      for(int i=0;i<nums.size();i++){
        if(nums[i]==1){count++;}
        else{
          sam.push_back(count);count=0;
        }} if(count>0){sam.push_back(count);}
         sort(sam.begin(),sam.end());
         return sam.back();
    }
};