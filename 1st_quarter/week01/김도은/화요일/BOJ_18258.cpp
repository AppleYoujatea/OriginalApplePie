#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int n;
    
    cin >> n;
    
    queue<int> st;
    
    for(int i = 0; i < n; i++){
        
        string str;
        
        cin >> str;
        
        if(str == "push"){
            int a;
            
            cin >> a;
            
            st.push(a);
        }
        else if (str == "front"){
            if(st.empty()){
                cout << "-1\n";
            }
            else{
                cout << st.front() << "\n";
            }
        }
        else if (str == "back"){
            if(st.empty()){
                cout << "-1\n";
            }
            else{
                cout << st.back() << "\n";
            }
        }
        else if(str == "pop"){
            if(st.empty()){
                cout << "-1\n";
            }
            else{
                cout << st.front() << "\n";
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


