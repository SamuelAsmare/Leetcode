class Solution {
public:
bool unique(vector<int>& arr, int number){
    for(int i=0; i<arr.size(); i++){
        if(arr[i]==number){return false;}
    }    return true;
}
int minimumOperations(vector<int>& nums) {
      vector<int> uniqueelements; int counter=0;
      for(int i=0; i<nums.size(); i++){
        if(unique(uniqueelements,nums[i])){
         uniqueelements.push_back(nums[i]);
            counter++;}} 
            for(int i=0;i<uniqueelements.size();i++){
                if(uniqueelements[i]==0){return counter-1;}}
 return counter;}
};