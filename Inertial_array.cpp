#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int i;
int arr[6]={0};
for(int i=0;i<=5;i++){
    cout<<"enter the value of ["<<i<<"]";
    cin>>arr[i];

}
sort(arr, arr+6);

bool largereven=false;
bool odd=false;
bool everyodd=false;


if((arr[5]%2==0)){
   largereven=true;
}

for(int i=0;i<=5;i++){
    if(arr[i]%2!=0){
      odd=true;
        break;
        
    }
}

for(int i=0;i<=5;i++){
    if(arr[i]%2!=0){
        for(int j=0;j<=5;j++){
            if(arr[j]%2==0&&arr[j]!=arr[5]&&arr[i]>=arr[j]){
            everyodd=true;
            }
        }

    }

}
if(odd && everyodd && largereven){
    cout<<"Inertial";
    }


else{
    cout<<"Not inertial";
}


    return 0;}
    

    
    
    