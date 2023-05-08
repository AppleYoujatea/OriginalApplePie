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




int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    string st;
    cin >> st;
    
    string ans = "quack";
    int sizes = st.size();
    
    vector<int>v(sizes);
    vector<int>w(sizes);
    
    bool check = true;
    for(int i=0;i<sizes;i++){
        if(st[i] != 'q')
            continue;
        
        int idx = i;
        int cnt = 0;
        
        while(cnt < 5 && idx < sizes){
            if(v[idx] == 0 && st[idx] == ans[cnt]){
                v[idx] = 1;
                cnt++;
            }
            idx++;
        }
        if(cnt != 5)
            check = false;
        
        for(int j=i;j<idx;j++){
            w[j]++;
        }
    }
    
    int duck_num = 0;
    for(int i=0;i<sizes;i++){
        duck_num = max(duck_num, w[i]);
        
        if(w[i] == 0)
            check = false;
    }
    
    if(check)
        cout << duck_num;
    else
        cout << "-1";
    
    
    
    
    return 0;
    
}
