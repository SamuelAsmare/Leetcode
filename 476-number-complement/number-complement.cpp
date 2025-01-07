class Solution {
public:
    int findComplement(int num) {
    vector<int> sam;
    while(num>0){
        sam.push_back(num%2);
        num=num/2;
    }
    reverse(sam.begin(),sam.end());
    int size=sam.size();
    for(int i=0;i<size;i++){
        if(sam[i]==0){sam[i]=1;}
        else{sam[i]=0;} }
    int sum=0;    for(int i=0;i<sam.size();i++){
        sum=sum+(sam[i]*pow(2,size-i-1));
    }
        return sum;
    }
};