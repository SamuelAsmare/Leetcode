class Solution {
public:
    int hammingDistance(int x, int y) {
vector<int> bx; vector<int> by;
        int count1=0;
        while(x>=0){if(count1==32){ break;}
        bx.push_back(x%2);x=x/2;count1++;}
        int count2=0;while(y>=0){if(count2==32){ break; }
        by.push_back(y%2); y=y/2; count2++;  }  int count=0;
        for(int i=0;i<32;i++){if(bx[i]!=by[i]){count++;}}
        return count;
    }
};