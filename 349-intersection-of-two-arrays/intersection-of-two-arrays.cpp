class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> sam;
       
        for(int i=0;i<nums1.size();i++){
          bool intersect=false;
          for(int j=0;j<nums2.size();j++){
            if(nums1[i]==nums2[j]){
              intersect=true;       break;     }      }
          if(intersect){
            sam.push_back(nums1[i]); }  }
            sort(sam.begin(),sam.end());
            auto uniquelements=unique(sam.begin(),sam.end());
            sam.erase(uniquelements,sam.end());
            return sam;
    }
};