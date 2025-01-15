class Solution {
public:
int prefixCount(vector<string>& words, string pref) {
   int count=0;int length=pref.length();
   for(int i=0;i<words.size();i++){
    if(words[i].length()>=length){
            bool found =true;
        for(int j=0;j<length;j++){
          if(pref[j]!=words[i][j]){found=false;} }
         if(found){count++;} }  }
     return count;
    }
};