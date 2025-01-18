class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
       vector<char>sam;
  int min=strs[0].length(),temp=0,index=0;
     for(int i=0;i<strs.size();i++){
           temp=strs[i].length();
           if(temp<min){min=temp;index=i; }     }
     for(int i=0;i<min;i++){
      bool found=true;
      for(int j=0;j<strs.size();j++){
        if(strs[j][i]!=strs[index][i]){found=false;}}
        if(!found){break;}
        if(found){sam.push_back(strs[index][i]);}}
        string sami(sam.begin(), sam.end()); return sami;
    }
};