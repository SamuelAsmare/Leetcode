class Solution {
public:
    int commonFactors(int a, int b) {
        vector<int > sam;
        if(a>b){
        for(int i=1;i<=b;i++){
            if(a%i==0 && b%i==0){sam.push_back(i);}
        }}
        else{
            for(int i=1;i<=a;i++){
                if(a%i==0 && b%i==0){sam.push_back(i); }
        }}
        return sam.size();

    }
};