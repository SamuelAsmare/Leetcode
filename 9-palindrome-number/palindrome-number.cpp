class Solution {
public:
    bool isPalindrome(int x) {
    string changedtostring=to_string(x);
    string reversed=changedtostring;
    reverse(reversed.begin(),reversed.end());
    return changedtostring==reversed;
        
    }
};