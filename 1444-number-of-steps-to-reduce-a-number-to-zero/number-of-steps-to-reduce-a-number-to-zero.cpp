class Solution {
public:
    int numberOfSteps(int num) {
       int numberofsteps=0;
  while(num>0){
    if(num%2==0){ num=num/2;}
    else{num=num-1;} numberofsteps++;
  }return numberofsteps; 
    }
};