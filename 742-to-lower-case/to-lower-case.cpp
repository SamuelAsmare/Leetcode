class Solution {
public:
    string toLowerCase(string s) {
        if(s.length()>100||s.length()<1){return "error";}
        for(int i=0;i<s.length();i++){
            
            s[i]=tolower(s[i]);
        }    return s;
    }
};