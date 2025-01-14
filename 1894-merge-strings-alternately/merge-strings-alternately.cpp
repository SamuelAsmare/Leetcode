class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int size1=word1.length();int size2=word2.length();
        vector<char>sam;
        if(size1>size2){
          for(int i=0;i<size2;i++){
               sam.push_back(word1[i]);
               sam.push_back(word2[i]);
                }
          for(int i=size2;i<size1;i++){ sam.push_back(word1[i]); }
        }
        else if(size1<size2){
          for(int i=0;i<size1;i++){
               sam.push_back(word1[i]);
               sam.push_back(word2[i]);
          }
          for(int i=size1;i<size2;i++){ sam.push_back(word2[i]); }}
          else{
            for(int i=0;i<size2;i++){
               sam.push_back(word1[i]);
               sam.push_back(word2[i]);  } }

               string str(sam.begin(),sam.end());
               return str;
    }
};