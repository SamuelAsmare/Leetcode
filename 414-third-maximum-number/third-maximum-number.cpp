class Solution {
public:
    int thirdMax(vector<int>& nums) {
        vector<int> sam;
        for(int i=0; i<nums.size(); i++){
        bool found=true;for(int j=1; j<=sam.size(); j++){

        if(nums[i]==sam[j-1]){     found=false;    }   }
        if(found){ sam.push_back(nums[i]);      }   }
    for(int i=0;i<sam.size();i++){
   for(int j=0;j<sam.size();j++){
       if(sam[i]>sam[j]){int temp=sam[i];
            sam[i]=sam[j];   sam[j]=temp;  } } }
     if(sam.size()<=2){
         return sam[0];      }
      else{return sam[2];} 
    }
};