#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<iomanip>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int n, s;
    
    cin >> n >> s;
    
    vector<int> v;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        v.push_back(a);
    }
    
    int start = 0, end = 0;
    long long sum = 0;
    int min = 100010;
    
    for(int i = 0; i <= n; i++){
        if(sum < s){
            sum += v[end];
            end++;
        }
        else{
            if(end - start < min){
                min = end - start;
            }
            
            if(start < n - 1){
                sum -= v[start];
                start++;
                i--;
            }
        }
    }
    
    if(min == 100010){
        cout << 0;
    }
    else{
        cout << min;
    }
    
}
