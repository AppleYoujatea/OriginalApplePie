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
    
    int arr[1001];
    int sum = 0;
    int dp[1001];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    sort(arr, arr + n);
    
    dp[0] = arr[0];
    for(int i=0;i<n-1;i++){
        dp[i+1] = dp[i] + arr[i+1];
    }
    
    for(int i=0;i<n;i++){
        sum += dp[i];
    }

    cout << sum;
    
//    for(int i=0;i<n;i++){
//        cout << dp[i] << '\n';
//    }
//
    
   
    return 0;
    
}


// 3
// 4
// 8
// 11
// 13

// 15 11 13
// 39

// 1 2 3 3 4

// 1
// 3
// 6
// 9
// 13

// 32


