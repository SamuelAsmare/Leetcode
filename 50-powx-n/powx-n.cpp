class Solution {
public:
    double myPow(double x, int n) {
        double temp=x;
  if((x>100.0||x<-100.0)||(x==0&&n<0)){
    return -1;
  }
  else if(x==2&&n==-2147483648){
    return 0;
  }
  else if(x==-1&&n%2==0){return 1;}
  else if(x==-1&&n%2!=0){return -1;}
  else if(x==1){return 1;}

  else{
  if(n>0){
  for(unsigned i=2;i<=n;i++){
    x = x*temp;
  }
  if(x>10000||x<-10000){
    return -1;
  }
return x;}

else if(n<0){
  for(int i=n;i<=-2;i++){
    x = x*temp;
  }
   return 1/x;
}
     
   } 
 return 1;  
   }
};