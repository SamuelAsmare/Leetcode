class Solution {
public:
    int lengthOfLastWord(string s) {
     vector<char> sam;
     int index;int count =0;
        for(int i=0;i<s.length();i++){
         sam.push_back(s[i]);  }
         reverse(sam.begin(), sam.end());
         for(int i=0;i<sam.size();i++){if(sam[i]!=' '){index=i; break;}}
      for(int i=index;i<sam.size();i++){
         if(sam[i]==' '){break;} 
           count++;      }
         return count; 
    }
};