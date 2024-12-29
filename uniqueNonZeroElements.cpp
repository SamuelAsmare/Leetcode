#include <iostream>
#include <vector>
#include <algorithm>
#include<string>
#include <cmath>
using namespace std;
int main(){
    int array[10]={10,0,10,10,0,10};
     int index=0;
    int sam[index];
    for(int i=0; i<10; i++){
        bool found=true;

        for(int j=0; j<=index; j++){

        if(array[i]==0 || array[i]==sam[j-1]){
            found=false;
        }
        }
        if(found){
            sam[index]=array[i];
            
        index++;
        }
    }
    

    for(int i=0; i<index; i++){ cout<<sam[i]<<" "; }
    return 0;
}
