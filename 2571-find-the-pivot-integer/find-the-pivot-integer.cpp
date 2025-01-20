class Solution {
public:
   bool pivot(int i=6, int n=8){
        int sum1=0,sum2=0;
        for(int j=1;j<=n;j++){
            if(j<=i){sum1=sum1+j;}
            if(j>=i &&  j<=n){sum2=sum2+j;}
        }return sum1==sum2;  }

int pivotInteger(int n) {
      for(int i=1;i<=n;i++){
        if(pivot(i,n)){return i;}
      }  return -1;    }
};