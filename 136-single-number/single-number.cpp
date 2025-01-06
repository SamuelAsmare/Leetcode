class Solution {
public:
    int singleNumber(vector<int>& nums) {
         int size=nums.size();
        int sam[size];
    
        for(int i=0;i<size;i++){
          bool found = true;
          for(int j=0;j<size;j++){
            if(i==j){
              continue;
            }
            else{
              if(nums[i]==nums[j]){
                found=false;
                break;
              
            }

        }
          
 }
 if (found){
          return nums[i];
          break;
        }
 }return 0;
        
        
    }
};