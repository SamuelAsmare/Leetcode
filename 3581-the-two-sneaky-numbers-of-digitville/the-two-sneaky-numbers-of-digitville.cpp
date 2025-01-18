class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
         vector<int> result;
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<nums.size();j++){
              if(i==j){continue;}
              if(nums[i]==nums[j]){result.push_back(nums[i]);break; }}
            sort(result.begin(),result.end());
            auto last=unique(result.begin(),result.end());
            result.erase(last,result.end());             
        }return result;
    }
};