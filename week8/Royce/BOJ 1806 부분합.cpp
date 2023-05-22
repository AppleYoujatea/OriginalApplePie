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

    ll s;
    cin >> n >> s;
    
    vector<int>v;
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        v.push_back(a);
    }
    
    ll sum = 0;
    ll ans = MAX;
    ll left = 0;
    ll right = 0;
    
    while(left <= right){
        
        if(sum >= s){
            ans = min(ans, right - left);
            sum -= v[left++];
        }
        // 넘을 때는 ans를 최소랑 비교해주고, sum에 제일 왼쪽 값을 더해주고, left를 옮긴다.
        else if(right == n)
            break;
        // right가 n에 오게 되면 넘으므로 break
        else{
            sum += v[right++];
        }
        // 넘지 못할 경우에는 그냥 제일 오른쪽 값을 더해주고, right만 증가시킨다.
        
    }
    
    if(ans == MAX)
        cout << 0;
    else
        cout << ans;
    
        
//        if(left == right){
//            if(v[left] >= s){
//                ans = 0;
//                check = true;
//                break;
//            }
//            else{
//                right++;
//            }
//        }
//        else{
//            sum += v[right];
//            if(sum < s){
//                right++;
//            }
//            else{
//                check = true;
//                ans = min(ans, right - left + 1);
//                left++;
//            }
//        }
//
//        if(right >= v.size()-1 || left >= v.size()-1)
//            break;
//    }
    
//    if(check){
//        cout << ans;
//    }
//    else{
//        cout << 0;
//    }
    
    
    return 0;
    
}
