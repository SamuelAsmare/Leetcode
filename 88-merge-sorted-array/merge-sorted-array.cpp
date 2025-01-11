class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
      vector<int> sam;
      for(int i=0; i<m; i++){
        sam.push_back(nums1[i]);
      }
      nums1.clear();
      for(int i=0; i<n; i++){
        sam.push_back(nums2[i]);
      }
      sort(sam.begin(), sam.end());
      for(int i=0;i<n+m;i++){
        nums1.push_back(sam[i]);  }
        for(int i=0;i<n+m;i++){
          cout<<nums1[i]<<" ";  }
    }
};