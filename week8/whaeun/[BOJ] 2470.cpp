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
    
    int n;
    
    cin >> n;
    
    vector<int> v;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        v.push_back(a);
    }
    
    sort(v.begin(), v.end());
    
    int start = 0, end = n-1;
    
    int minNum = 2000000010;
    
    int ans1 = 0, ans2 = 0;
    
    while(start < end){
        int sum = v[start] + v[end];
        
        if(abs(sum) < minNum){
            ans1 = v[start];
            ans2 = v[end];
            minNum = abs(sum);
        }
        
        if(sum < 0){
            start++;
        }
        else{
            end--;
        }
        
    }
    
    cout << min(ans1, ans2) << " " << max(ans1, ans2);
    
}



