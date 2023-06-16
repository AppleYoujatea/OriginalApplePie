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
    
    for(int i=0;i<n;i++){
        
        stack<int>s;

        string st;
        cin >> st;
        
        bool flag = false;
        for(int j=0;j<st.length();j++){
            if(st[j] == '('){
                s.push('(');
            }
            else if(st[j] == ')' && !s.empty()){
                s.pop();
            }
            else if(st[j] == ')' && s.empty()){
                flag = true;
            }
        }
        
        if(!s.empty()){
            flag = true;
        }
        
        if(flag){
            cout << "NO" << '\n';
        }
        else{
            cout << "YES" << '\n';
        }
        
    }
    
   
    return 0;
    
}
