class Solution {
public:

vector<int> findDisappearedNumbers(vector<int>& nums) {
    sort(nums.begin(),nums.end());
      int size = nums.size(); vector<int>sam;
    for(int i=1;i<=size;i++){
      if(!(binary_search(nums.begin(),nums.end(),i))){
            sam.push_back(i); }}            
      return sam;       
    }
};