class Solution {
public:
    bool isThree(int n) {
        vector<int> sam;
        for(int i=1;i<=n;i++){
            if(n%i ==0){sam.push_back(i);
                             }
        }
        if(sam.size()==3){return true;}
        return false;
    }
}; 