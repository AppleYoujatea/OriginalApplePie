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
#define mod1 1000000000
#define mod 1000000007
#define pii pair<int, int>
using ll = long long;
using namespace std;
int n,m,k;
int l,r,t;
int h;


string st[501];




int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    string s, t;
    while(cin >> s >> t){
        int idx = 0;
        bool check = false;
        
        for(int i=0;i<t.length();i++){
            if(s[idx] == t[i]){
                idx++;
            }
            
            if(idx == s.length()){ // s의 길이의 끝까지 오면 같은게 그만큼 있으므로, break
                check = true;
                break;
            }
        }
        
        if(check){
            cout << "Yes" << '\n';
        }
        else{
            cout << "No" << '\n';
        }
    }
    
    
    
    
    return 0;
    
}
