#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>

using namespace std;

char arr[5] = {'q', 'u', 'a', 'c', 'k'};
//quackq

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    string str;
    
    cin >> str;
    
    int answer = 0;
    bool check_ans = true;
    
    for(int i = 0; i < str.length()/4; i++){
        int check = false;
        int idx = 0;
        
        for(int j = 0; j < str.length(); j++){
            if(arr[idx] == str[j]){
                idx++;
                str[j] = '0';
                
                idx %= 5;
                
                if(!check){
                    check = true;
                }
            }
        }
        
        if(idx != 0){
            check_ans = false;
        }
        
        if(check){
            answer++;
        }
    }
    
    for(int i = 0; i < str.length(); i++){
        if(str[i] != '0'){
            check_ans = false;
        }
    }
    
    if(check_ans){
        cout << answer;
    }
    else{
        cout << -1;
    }
    
    
    
}
