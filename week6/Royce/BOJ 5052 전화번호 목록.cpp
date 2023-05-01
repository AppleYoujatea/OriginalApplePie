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

    
    
    cin >> t;
    
    while(t--){
        
        bool check = false;
        cin >> n;
        vector<string>v;

        for(int i=0;i<n;i++){
            string st;
            cin >> st;
            v.push_back(st);
        }
        
        sort(v.begin(), v.end());
        // 벡터들을 정렬해서 제일 짧은게 앞으로 오게 한다.
        
        for(int i=0;i<n-1;i++){
            string s = v.at(i);
            string t = v.at(i+1);
            
            if(s.length() >= t.length())
                continue;
            if(s == t.substr(0, s.size())){
                cout << "NO" << '\n';
                check = true;
                break;
            }
            
        
            // 지금의 단어가 다음 단어보다 길이가 같거나 길면 넘어가기
            // 이렇게 하면 같은 경우도 포함된다.
            
            // next의 경우에서 0부터 now의 길이만큼 자른 것이 v[k]와 같다면 false이므로 break
        }
        
        if(!check)
            cout << "YES" << '\n';
        
        
    }
    
    
    
    
    return 0;
    
}
