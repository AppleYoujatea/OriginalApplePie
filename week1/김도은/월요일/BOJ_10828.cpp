#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main(){
    
    int n;
    
    cin >> n;
    
    stack<int> st;
    
    for(int i = 0; i < n; i++){
        
        string str;
        
        cin >> str;
        
        if(str == "push"){
            int a;
            
            cin >> a;
            
            st.push(a);
        }
        else if (str == "top"){
            if(st.empty()){
                cout << "-1\n";
            }
            else{
                cout << st.top() << "\n";
            }
        }
        else if(str == "pop"){
            if(st.empty()){
                cout << "-1\n";
            }
            else{
                cout << st.top() << "\n";
                st.pop();
            }
        }
        else if(str == "size"){
            cout << st.size() << "\n";
        }
        else if(str == "empty"){
            if(st.empty()){
                cout << "1\n";
            }
            else{
                cout << "0\n";
            }
        }
        
    }
}

//
