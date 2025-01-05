class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
    
        
  int size1 = nums.size();
for(int i=0;i<size1;i++){
    if(nums[i]<-10000||nums[i]>10000){
        return -1;
        
    }
  }
  if(size1<1||size1>10000){
   return -1;
   
  }
  else if(target<-10000||target>10000){
    return -1;
  } 
  
  else{

    for(int i=0;i<size1;i++){
    if(nums[i]==target){
     return i;
      
    }} 
    for(int i=0;i<size1-1;i++ ){
     if((target>nums[i])&&(target<nums[i+1])){
     return i+1;
    }
    }
    for(int i=0;i<size1;i++){
    if(target<nums[0]){
     return 0;
    
    } 
    
  }
  return size1;

  
  }



    }};