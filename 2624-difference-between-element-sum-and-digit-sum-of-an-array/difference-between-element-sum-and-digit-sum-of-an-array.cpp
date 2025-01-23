class Solution {
public:
    int digits(int n){
    int digitssum=0;
    while(n>0){
     digitssum=digitssum+(n%10);  
     n=n/10; }
     cout<<" Digits: "<<digitssum<<endl;
                 
     return digitssum;
  }
int differenceOfSum(vector<int>& nums) {
        int elements=0, digit=0;
        for(int i=0;i<nums.size();i++){
            elements=elements+nums[i];
            digit=digit+digits(nums[i]);
        }
        
        cout<<elements<<" "<<digit<<endl;
        return elements-digit;
    }
};