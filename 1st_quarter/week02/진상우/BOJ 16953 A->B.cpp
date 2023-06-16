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

    
    ll a, b;
    cin >> a >> b;
    
    int cnt = 0;
    bool flag = false;
    while(1){
        
        if(a == b){
            break;
        }
        else if(a > b){
            flag = true;
            cnt = -2;
            break;
        }
        else if(b % 10 != 1 && b % 2 != 0 && a != b){
            flag = true;
            cnt = -2;
            break;
        }
        else if(b % 10 != 1 && b % 2 == 0){
            b /= 2;
            cnt++;
        }
        else if(b % 10 == 1){
            b = (b / 10);
            cnt++;
        }
        
        if(flag)
            break;
        
    }
    
    cout << cnt + 1;
    
    
    
    
   
    return 0;
    
}


// 162
// 81
// 8
// 4
// 2

