class Solution {
public:
int firstMissingPositive(vector<int>& nums) {
    sort(nums.begin(),nums.end());
    for(int i=1;i>=1;i++){
      if(!(binary_search(nums.begin(),nums.end(),i))){return i;}
    }       
    return -1;     
          }    
    
};