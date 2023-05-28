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
    
    int arr[100001];
    int mist[100001];
    for(int i=1;i<=n;i++){
        cin >> arr[i];
    }
    int num = 0;
    for(int i=1;i<=n;i++){
        if(arr[i] > arr[i+1])
            num++;
        mist[i+1] = num;
        // 실수가 있을 경우에 mist에 넣어줌
        // num은 계속 증가하므로 누적해서 들어간다.
    }
    
    cin >> m;
    for(int i=0;i<m;i++){
        int a, b;
        cin >> a >> b;
        cout << mist[b] - mist[a] << '\n';
    }
    
    
    
//    cin >> m;
//    for(int i=0;i<m;i++){
//        int a, b;
//        cin >> a >> b;
//
//        int num = 0;
//        if(a == b){
//            cout << 0 << '\n';
//        }
//        else{
//            int idx = a;
//            while(1){
//                if(idx == b)
//                    break;
//                if(v[idx-1] > v[idx])
//                    num++;
//                idx++;
//            }
//            cout << num << '\n';
//        }
//
//    }
    // i > i+1이면 실수
    
    
    return 0;
    
}
