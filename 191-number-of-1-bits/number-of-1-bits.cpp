class Solution {
public:
    int hammingWeight(int n) {
        if(n<0) return -1; int count = 0;
        while(n>0){    if(n%2==1){  count++;  }
        n=n/2;} return count;    }
    
};