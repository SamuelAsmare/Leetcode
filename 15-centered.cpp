//This code is to check whether the given array is 15 - centered or not.
#include<iostream>
using namespace std;
void mainprinter()
{
    int n;
    cout<<"Enter the number of elements: ";
    cin>>n;
    int sam[n]={}; 
    for(int i=0; i<n; i++)
    {
        cout<<"Enter element sam["<<i<<"]: ";
        cin>>sam[i];
    }
    int sum=0,counter,left,right; bool centered=false;
    for(int i=0; i<n; i++)
    {
        sum=sum+sam[i];
    }
    cout<<sum<<endl;

       
       for(int left=0; left<n/2; left++)
      {
         for (int right=n-1-left; right>=n-1-left ; right--)
         {
            sum=sum-sam[left]-sam[right];
            if(sum==15)
            {
               centered=true;
            }
     
         }
      }
           
   if(centered)
   {
     cout<<"15 centered"<<endl;
   }else
   { cout<<"nooks"<<endl;
   }
  }
  int main()
{
    mainprinter();
     return 0;
}
