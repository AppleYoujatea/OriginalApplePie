#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<cmath>

using namespace std;

int main(){
    
    int testcase;
    
    cin >> testcase;
    
    for(int t = 0; t < testcase; t++){
        int n;
        vector<string> v;
        bool check = true;
        
        cin >> n;
        
        for(int i = 0; i < n; i++){
            string str;
            
            cin >> str;
            
            v.push_back(str);
        }
        
        sort(v.begin(), v.end());
        
        for(int i = 1; i < n; i++){
            if(v[i-1].substr(0, min(v[i].length(),v[i-1].length())) == v[i].substr(0, min(v[i].length(),v[i-1].length())) ){
                check = false;
            }
        }
        
        if(check){
            cout << "YES\n";
        }
        else{
            cout << "NO\n";
        }
        
        
    }
    
}
