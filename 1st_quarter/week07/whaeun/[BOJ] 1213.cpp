#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>

using namespace std;

int arr[27];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    string str;
    
    cin >> str;
    
    for(int i = 0; i < str.length(); i++){
        arr[str[i] - 'A'] += 1;
    }
    
    int odd_cnt = 0;
    char center;
    
    vector<char>ans;
    
    for(int i = 0; i < 27; i++){
        if(arr[i] % 2 == 1){
            odd_cnt++;
            center = i + 'A';
        }
        
        for(int j = 0; j < arr[i] / 2; j++){
            ans.push_back(i+'A');
        }
    }
    
    if(odd_cnt == 0){
        for(int i = 0; i < ans.size(); i++){
            cout << ans[i];
        }
        for(int i = ans.size()-1; i >= 0; i--){
            cout << ans[i];
        }
        
    }
    else if(odd_cnt == 1){
        for(int i = 0; i < ans.size(); i++){
            cout << ans[i];
        }
        
        cout << center;
        
        for(int i = ans.size()-1; i >= 0; i--){
            cout << ans[i];
        }
        
    }
    else{
        cout << "I'm Sorry Hansoo";
    }
}
