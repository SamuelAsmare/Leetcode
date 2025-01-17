class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> sam;
        for(int i=0;i<words.size();i++){
          for(int j=0;j<words[i].length();j++){
            if(words[i][j]==x){sam.push_back(i);break;}}}
        return sam;
    }
};