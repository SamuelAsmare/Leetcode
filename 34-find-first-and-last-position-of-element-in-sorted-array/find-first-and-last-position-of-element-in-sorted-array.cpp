class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        if (!n) return {-1,-1};
        int left = 0 , right = n-1 , first_occurence;
    //  first occurance
        while(left < right){
            int mid = left + (right - left)/2;
            if (nums[mid] >= target){
                right = mid;}
            else {
                left = mid + 1;
            }
        }
        if (nums[left] == target){
           first_occurence = left;
        }
        else{
            return {-1,-1};
        }
    //  last occurence
    left = 0 , right = n-1 ;
    while(left < right){
            int mid = left + (right - left + 1)/2;
            if (nums[mid] <= target){
                left = mid;}
            else {
                right = mid-1;
            }
        }
        return {first_occurence,left};        
    }
};