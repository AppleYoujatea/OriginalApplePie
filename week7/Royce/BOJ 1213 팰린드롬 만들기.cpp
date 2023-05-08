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


int alp[26];


int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    string st;
    cin >> st;
    
    for(int i=0;i<st.size();i++){
        alp[st[i] - 'A']++;
    }
    
    int mid = -1;
    int diff = 0;
    
    for(int i=0;i<26;i++){
        if(alp[i] > 0){
            if(alp[i] % 2 == 1){
                mid = i;
                alp[i]--;
                diff++;
            }
        }
    }
    
    if(diff > 1)
        cout << "I'm Sorry Hansoo" << '\n';
    else{
        string ans = "";
        string tmp = "";
        for(int i=0;i<26;i++){
            if(alp[i] > 0){
                for(int j=0;j<alp[i]/2;j++){
                    ans += i + 'A';
                }
            }
        }
        tmp = ans;
        reverse(tmp.begin(), tmp.end());
        if(mid != -1){
            ans += mid + 'A';
        }
        ans += tmp;
        cout << ans << '\n';
    }
    
    
    
    
    
    
    
    
    return 0;
    
}
