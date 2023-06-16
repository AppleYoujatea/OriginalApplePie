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
    ios::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);
        
    int n, m, a;
    
    cin >> n;
    
    map<int, int> dic;
    
    for(int i = 0; i< n; i++){
        cin >> a;
        dic[a]++;
    }
    
    cin >> m;
    
    for(int i = 0; i < m; i++){
        cin >> a;
        
        cout << dic[a] << " ";
    }
}

