class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
     vector<char> sam1,sam2;
  for(int i=0;i<s1.length();i++){sam1.push_back(s1[i]);}
  for(int i=0;i<s1.length();i++){sam2.push_back(s2[i]);}
  if(s1==s2){return true;}
      sort(s1.begin(), s1.end());sort(s2.begin(), s2.end());
      if(s1!=s2){return false;} int count=0;
      for(int i=0;i<sam1.size();i++){
         if(sam1[i]!=sam2[i]){count++;} }
         if(count>2){   return false;  }
         return true;
    }
};