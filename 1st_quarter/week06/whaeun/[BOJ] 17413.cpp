#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>

using namespace std;

int main(){
    
    string str;
    
    stack<char> st;
    queue<char> q;
    
    bool check = false;
    
    getline(cin, str);
    
    for(int i = 0; i < str.length(); i++){
        if(str[i] == '<' || (str[i] != '>' && check == true)){
            check = true;
            if(!st.empty()){
                while(!st.empty()){
                    cout << st.top();
                    st.pop();
                }
            }
            q.push(str[i]);
        }
        else if(str[i] == '>'){
            while(!q.empty()){
                cout << q.front();
                q.pop();
            }
            cout << '>';
            check = false;
        }
        else if(str[i] == ' '){
            if(!st.empty()){
                while(!st.empty()){
                    cout << st.top();
                    st.pop();
                }
            }
            cout << " ";
        }
        else{
            st.push(str[i]);
        }
    }
    
    if(!st.empty()){
        while(!st.empty()){
            cout << st.top();
            st.pop();
        }
    }
    
    
    
}
