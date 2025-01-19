class Solution {
public:
bool digitcounter(int n){
  int count=0;
   while(n>0){
      n=n/10;count++;
    }return count%2==0;
}
int findNumbers(vector<int>& nums) {
  int counter=0;
        for(int i=0;i<nums.size();i++){
             if(digitcounter(nums[i])){counter++;}
        }return counter;
    }
};