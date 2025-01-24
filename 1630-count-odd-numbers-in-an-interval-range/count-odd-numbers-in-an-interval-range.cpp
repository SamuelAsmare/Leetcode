class Solution {
public:
   int countOdds(int low, int high) {
    int counter=0; int i=low;
    while(i<=high){
        if(i%2!=0){
            counter++;
            
        }i++;
    }return counter;  }
    
};