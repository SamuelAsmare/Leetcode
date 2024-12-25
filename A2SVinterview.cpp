    #include <iostream>
    #include <vector>
    #include <unordered_set>
    #include<algorithm>
    using namespace std;

    int main() {
    
        
        int numbers;
        cout<<"how manny numbers do you want::} ";
        cin>>numbers;
        int sam[numbers]={};
        
        for(int i=0;i<numbers;i++){
            cout<<"Enter ["<<i<<"]";
            cin>>sam[i];}
            sort(sam,sam+numbers);
        int sum=0;
        int counter=0;
        for (int i=0;i<numbers;i++){
            sum=sum+sam[i];

             counter=counter+1;
                if (sum>=5000){
                break;
             }
             
             }
        
        cout<<counter-1<<endl;
        
        return 0;
    }