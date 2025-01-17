class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int finalresult=0;
        for(int i=0; i<operations.size();i++){
          if(operations[i]=="X++"||operations[i]=="++X"){
           finalresult++;      }
           else if(operations[i]=="X--"||operations[i]=="--X"){
            finalresult--;     }
        }return finalresult;
    }
};