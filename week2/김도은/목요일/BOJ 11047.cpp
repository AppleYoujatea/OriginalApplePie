#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <stack>
#include <cstring>
#include <climits>
#include <cstdio>
#include <set>
#include <map>

#define MAX 1000010
#define INF 1e9
#define MOD 1e9+7

using namespace std;

vector<int> coin;

int main(){
    
    int n, k;
    int cnt = 0;
    
    cin >> n >> k;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        coin.push_back(a);
    }
    
    for(int j = n-1; j >= 0; j--){
        if(k >= coin[j]){
            while(k >= coin[j]){
                k -= coin[j];
                cnt++;
            }
        }
    }
    
    cout << cnt;
}
