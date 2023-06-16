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
    long long n, answer = 0;
    
    cin >> n;
    
    int i = 1;
    
    while(n >= 0){
        
        if(n-i > i){
            n -= i;
            i++;
            answer++;
        }
        else{
            answer++;
            break;
        }
    }
    
    cout << answer;
    
}
