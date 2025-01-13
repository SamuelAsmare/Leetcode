class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
      vector<char> sam;
        bool exists = false;
        for(int i = 0; i < letters.size();i++){
          if(target<letters[i]){exists = true;}
          if(exists){
          if(letters[i] > target){ sam.push_back(letters[i]); }}   }
        sort(sam.begin(), sam.end());
        if(!exists){return letters[0];}
        return sam[0];
        
    }
};