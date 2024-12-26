#include<iostream> 
using namespace std;
int main(){
  int number1; cout<<"Enter the first number::   ";  cin>>number1;
  int sam[100]={};
  int sami[100]={};
  int index=0;
  int index2=0;
  int number2; cout<<"Enter the second number::   "; cin>>number2;
  int index3=0;
  int final[100]={};
  for(int i=1;i<=number1;i++){
    if(number1%i==0){
      sam[index]=i;
      index++;}

  }
 
  
  for(int i=1;i<=number2;i++){
    if(number2%i==0){
      sami[index2]=i;
      index2++;}

  }
 


for(int i=0;i<=index-1;i++){
  for(int j=0;j<=index2-1;j++){
    if(sam[i]==sami[j]){
      final[index3]=sam[i];
      index3++;

    }}
  }

  cout<<"GCF of the numbers you  have given is  "<<final[index3-1];


  
  return 0;
}
/*
Using vector::



int main(){
  int number1; cout<<"Please enter the first number:: "; cin>>number1;
  int number2; cout<<"Please enter the second number:: "; cin>>number2;
 vector<int> sam;
 vector<int> sami;
 
  int index3=0;
  vector<int> final;
  for(int i=1;i<=number1;i++){
    if(number1%i==0){
      sam.push_back(i);

  }}
 
  
  for(int i=1;i<=number2;i++){
    if(number2%i==0){
      sami.push_back(i);

  }
  }

  int size1=sam.size();
  int size2=sami.size();


for(int i=0;i<size1;i++){
  for(int j=0;j<size2;j++){
    if(sam[i]==sami[j]){
      final.push_back(sam[i]);
    }}
  }
  int size=final.size();
  

  
  cout<<"GCF of the numbers you  have given is  "<< final[size-1];
  

  
  return 0;
}

*/