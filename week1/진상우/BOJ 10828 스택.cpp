#include <iostream>  // stdio.h 와 같은 것
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <cstring>
#include <cmath>
#include <functional>
#include <map>
#include <unordered_map>
#include <set>
#include <sstream>

// control i
#define MAX 987654321
#define mod 1000000000
#define pii pair<int, int>
using ll = long long;
using namespace std;
int n,m,k;
int l,r,t;
int h;




int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    
    stack<int>s;
    for(int i=0;i<n;i++){
        
        string st;
        int a;
        cin >> st;
        
        if(st == "push"){
            cin >> a;
            s.push(a);
        }
        else if(st == "pop" && !s.empty()){
            cout << s.top() << '\n';
            s.pop();
        }
        else if(st == "pop" && s.empty()){
            cout << "-1" << '\n';
        }
        else if(st == "size"){
            cout << s.size() << '\n';
        }
        else if(st == "empty"){
            if(s.empty())
                cout << 1 << '\n';
            else
                cout << 0 << '\n';
        }
        else if(st == "top" && !s.empty()){
            cout << s.top() << '\n';
        }
        else if(st == "top" && s.empty())
            cout << -1 << '\n';
        
    }
    
   
    return 0;
    
}
