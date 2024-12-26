#include<iostream>
using namespace std;
int centered(int arr[], int n);
int main(){
int n, num;
cout<<"enter the array size: ";
cin>>n;
int* arr = new int[n];
cout<<"enter each elements of the array: "<<endl;
for(int i=0;i<n;i++){
cin>>num;
arr[i] = num;
}
cout<<endl<<endl<<endl<<centered(arr,n);
return 0;
}
int centered(int arr[], int n){
int sum = 0, last = n-1, mid = n/2; 
for(int i=0;i<n;i++){
sum += arr[i];
}
for(int j=0;j<mid;j++){
if(sum == 15) return 1;
sum = sum - (arr[j] + arr[last]);
last--;
}
return 0;
}