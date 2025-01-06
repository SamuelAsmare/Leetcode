class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
   int size=nums.size();
   if(size>10000||size<1){  return -1;   }
   for(int i=0; i<size;i++){    if(nums[i]>size||nums[i]<0){  return -1;}   } 
    int start = nums[0];
    int end = size;
      
     for(int i=start; i<=size; i++){       bool exists = false; 
          for(int j=0;j<size;j++){        
        if(nums[j]==i){       exists = true;          break;     }}
     if(!exists){      return i;     }      }       return 0; 
        
    }
};