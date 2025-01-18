class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> sam;
        for(int i=0;i<nums.size();i++){
          for(int j=0;j<nums.size();j++){
            if(i==j){continue;}
          if((nums[i]+nums[j])==target){sam.push_back(i);
          sam.push_back(j);
          break;
          
           }      } }
           sort(sam.begin(),sam.end());
           auto makeitunique=unique(sam.begin(),sam.end());
           sam.erase(makeitunique,sam.end());
          
        return sam;
        
    }
};