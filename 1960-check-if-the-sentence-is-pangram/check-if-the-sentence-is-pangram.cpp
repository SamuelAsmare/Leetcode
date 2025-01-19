class Solution {
public:
    bool checkIfPangram(string sentence) {
        vector<char> sam;
       for(int i=0;i<sentence.length();i++){
        sam.push_back(sentence[i]); }
        sort(sam.begin(),sam.end()); 
        auto uniquelements=unique(sam.begin(),sam.end());
        sam.erase(uniquelements,sam.end());
         for(int i=97;i<=122;i++){
            if(sam[abs(i-97)]!=char(i)){return false;}
         }return true;
    }
};