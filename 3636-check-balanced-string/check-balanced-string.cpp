class Solution {
public:
    bool isBalanced(string num) {
        int sumodd=0,sumeven=0;
        for(int i=0;i<num.length();i++){
            if(i%2!=0){
              sumodd=sumodd+(num[i]-'0');
            }
            else{
                sumeven=sumeven+(num[i]-'0');
        }}return sumodd==sumeven;
    }
};