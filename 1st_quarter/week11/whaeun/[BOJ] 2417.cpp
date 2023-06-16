#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<iomanip>

#define MAX 1000000007

using namespace std;

int main(){
    unsigned long long n;
    
    cin >> n;
    
    long long ans = sqrt(n);
    
    if(ans * ans < n){
        cout << ans + 1;
    }
    else{
        cout << ans;
    }
    
}
