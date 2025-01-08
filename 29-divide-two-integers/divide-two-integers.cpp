
class Solution {
public:
    int divide(int dividend, int divisor) {
     int tempx=divisor; int tempy=dividend; long long v,w;unsigned counter=0;
         if(divisor==0){return -1;}
         if(dividend==divisor){

             return 1;};
        
        if((dividend<=INT_MAX&&dividend>-2147483648)&&divisor<=INT_MAX){
            if(divisor==1){return dividend;}
            if(divisor==-1){return -dividend;}
            
        }
        v=abs((long long)divisor);
        w=abs((long long)dividend);
    
    while(w>=v){counter++; w=w-v; }


    int result;
    if((tempx<0&&tempy>0)||(tempx>0&&tempy<0)){result=-counter; return result;}
    else{
        if(counter>INT_MAX){return INT_MAX;}
        return counter;    }
  }
}
;
