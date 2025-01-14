class Solution {
public:
    int firstUniqChar(string s) {
        int length=s.length();
        for(int i=0;i<length;i++){
          bool unique=true;
          for(int j=0;j<length;j++){
            if(i==j){continue;}
          if(s[j]==s[i]){unique=false;break; }
          }
          if(unique){return i;} }
          return -1;
    }
};