class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    vector<int> combine;
  int size1 = nums1.size();
  int size2 = nums2.size();

  for(int i = 0; i < size1;i++){
    combine.push_back(nums1[i]);
  }
  for(int i = 0; i < size2;i++){
    combine.push_back(nums2[i]);
  }
  sort(combine.begin(), combine.end());
   for(int i = 0; i <=size1+size2-1;i++){
 
}

//compute the median value;
if((size1+size2)%2==0){
  int medium=(size1+size2)/2;

  return double((combine[medium-1]+combine[medium])/2.0);
}
else if((size1+size2)%2!=0){
  int medium=(size1+size2)/2;
  return double(combine[medium]);

}    
    return 0;}
};