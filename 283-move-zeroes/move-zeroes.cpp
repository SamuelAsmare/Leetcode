class Solution {
public:
    void moveZeroes(vector<int>& nums) {
       vector<int> arr;
int size=nums.size(); if(size<1||size>10000){cout<<"error";}
for(int i = 0; i < size; i++) {
        if(nums[i] == 0) {
arr.push_back(nums[i]);   }    }
    int size2=arr.size();
   nums.erase(remove(nums.begin(), nums.end(),0),nums.end());
        
    
 for(int i=0; i < size2; i++) {
          nums.push_back(arr[i]);
 
 } for(int i=0; i < size; i++) {
    cout<<nums[i]<<" ";
 }
    }
};