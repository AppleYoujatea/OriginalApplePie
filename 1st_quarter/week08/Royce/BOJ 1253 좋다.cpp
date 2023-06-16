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
    
    vector<int>v;
    
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        v.push_back(a);
    }
    
    sort(v.begin(), v.end());
    
    int ans = 0;
    
    for(int i=0;i<n;i++){
        int left = 0;
        int right = n-1;
        
        while(left < right){
            if(left == i){
                left++;
                continue;
            }
            if(right == i){
                right--;
                continue;
            }
            // 자기자신을 가리키면 넘어가야 하므로, left의 경우 늘려주고, right의 경우 줄여주면서 찾아준다.
            if(v[i] > v[left] + v[right])
                left++;
            else if(v[i] == v[left] + v[right]){
                ans++;
                break;
            }
            else
                right--;
        }
        
    }
    
    cout << ans;
    
    
    
    return 0;
    
}
