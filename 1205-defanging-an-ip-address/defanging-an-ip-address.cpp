class Solution {
public:
    string defangIPaddr(string address) {
        vector<char>sam;
        for(int i=0;i<address.length();i++){
          if(address[i]=='.'){
           sam.push_back( '[');
            sam.push_back('.');
            sam.push_back(']');   }
          else{sam.push_back(address[i]);} }
         string final(sam.begin(), sam.end());
         address=final;   return address;
    }
};