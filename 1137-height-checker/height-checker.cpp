class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> sam;
        for(int i=0;i<heights.size();i++){
        sam.push_back(heights[i]);
        }sort(heights.begin(),heights.end()); int count=0;
        for(int i=0;i<heights.size();i++){
          if(sam[i]!=heights[i]){ count++;}  }
          return count;
    }
};