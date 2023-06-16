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
    queue<int>q;

    
    for(int i=0;i<n;i++){
        
        
        string st;
        cin >> st;
        
        if(st == "push"){
            int a;
            cin >> a;
            q.push(a);
        }
        else if(st == "pop"){
            if(q.empty()){
                cout << "-1" << '\n';
            }
            else{
                cout << q.front() << '\n';
                q.pop();
            }
        }
        else if(st == "size"){
            cout << q.size() << '\n';
        }
        else if(st == "empty"){
            if(q.empty()){
                cout << "1" << '\n';
            }
            else{
                cout << "0" << '\n';
            }
        }
        else if(st == "front"){
            if(q.empty()){
                cout << "-1" << '\n';
            }
            else{
                cout << q.front() << '\n';
            }
        }
        else if(st == "back"){
            if(q.empty()){
                cout << "-1" << '\n';
            }
            else{
                cout << q.back() << '\n';
            }
        }
        
    }
    
   
    return 0;
    
}
