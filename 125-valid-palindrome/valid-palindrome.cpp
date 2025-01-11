class Solution {
public:
    bool isPalindrome(string s) {
      vector<char> sam;
      for(int i=0; i<s.length(); i++)  {
        if(isalpha(s[i])||isdigit(s[i])){sam.push_back(tolower(s[i]));} }
           bool ispalindrome=true;
        for(int i=0; i<sam.size()/2; i++) {
          
          for(int j=sam.size()-1-i; j>=sam.size()-1-i; j--) {
            if(sam[j]!=sam[i]){ispalindrome=false;}       }
                 }  return ispalindrome;   
    }
};