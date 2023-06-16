#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

int main(){
    
    string str, str2;
    
    while(cin >> str >> str2) {
        
        bool check = false;
        
        int idx = 0;
        
        for(int i = 0; i < str2.length(); i++){
            if(str[idx] == str2[i]){
                idx++;
            }
            
            if(idx == str.length()){
                check = true;
                break;
            }
        }
        
        if(check) {
            cout << "Yes\n";
        }
        else{
            cout << "No\n";
        }
        
    }
}
