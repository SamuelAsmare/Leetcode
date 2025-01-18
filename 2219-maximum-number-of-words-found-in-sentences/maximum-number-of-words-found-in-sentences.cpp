class Solution {
public:
   int words(string  string ){
    int count=0;
    for(int i=0;i<string.length();i++){
      if(string[i]==' '){count++;} }
      return count+1;
  }

  int mostWordsFound(vector<string>& sentences) {
     int max=0;
        for(int i=0;i<sentences.size();i++){
         int temp=words(sentences[i]);
          if(temp>max){max=temp;}
        }return max;
    }
};