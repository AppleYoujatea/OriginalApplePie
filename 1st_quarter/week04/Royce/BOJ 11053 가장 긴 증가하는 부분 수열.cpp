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

    
    
    cin >> n;
    
    int dp[1001];
    int arr[1001];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    int ans = 0;
    for(int i=0;i<n;i++){
        dp[i] = 1;
        // 처음 한가지인 경우에는 1이므로 모두 1로 초기화
        
        for(int j=0;j<i;j++){
            if(arr[j] < arr[i])
                dp[i] = max(dp[i], dp[j]+1);
        }   // arr[j]가 i보다 더 인덱스가 작은데, 계속 arr[i]가 더 클경우에는
            // dp[i]는 dp[j]+1과 dp[i] 중 큰 것을 갱신한다.
        
        ans = max(ans, dp[i]);
        
    }
    
    cout << ans;
    
    return 0;
    
}
