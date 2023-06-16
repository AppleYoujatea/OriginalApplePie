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

    
    cin >> n >> k;
    
    vector<int>v;
    vector<int>vec;
    
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        v.push_back(a);
        if(a == 1)
            vec.push_back(i+1);
    }
    
    if(vec.size() < k){
        cout << "-1" << '\n';
        return 0;
    }
    // 1을 넣은 개수 자체가 적으면 불가능하므로 -1을 출력한다.
    
    int ans = MAX;
    for(int i=0;i<=vec.size()-k;i++){
        ans = min(ans, vec[i+k-1] - vec[i] + 1);
    }
    // k-1에서 0까지 + 1 과 라이온의 개수-1 에서 라이온의 개수-k까지에 1을 더한 값을 찾는다.
    // 그냥 제일 짧은 거리를 찾는다고 생각하면 된다.
    // 길이가 k를 만족하는..
    
    
    cout << ans;
    
//    int left = 0;
//    int right = 0;
//    int num = 0;
//    int ans = MAX;
//    bool check = false;
//
//    while(left <= right && right < n){
//        if(v[right] == 1){
//            num++;
//            if(num <= k && left < right){
//                ans = min(ans, right - left);
//                left++;
//                num--;
//                check = true;
//            }
//            else if(num <= k && left == right){
//                check = true;
//                ans = min(ans, right - left);
//                left++;
//                right++;
//                num--;
//            }
//        }
//        else{
//            right++;
//        }
//
//    }
//
//    if(check){
//        cout << ans;
//    }
//    else{
//        cout << "-1";
//    }
//
    
    
    return 0;
    
}
