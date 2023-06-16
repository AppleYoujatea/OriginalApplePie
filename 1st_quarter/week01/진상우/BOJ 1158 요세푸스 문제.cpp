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
#define mod 1000000000
#define pii pair<int, int>
using ll = long long;
using namespace std;
int n,m,k;
int l,r,t;
int h;




int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    cin >> n >> k;
    
    queue<int>q;
    
    for(int i=1;i<=n;i++){
        q.push(i);
    }
    
    cout << "<";
    
    int num = 0;
    int idx = 0;
    while(!q.empty()){
        num = q.front();
        q.pop();
        idx++;
        // num을 저장하고 pop해주고 idx를 증가시켜 이동한다.
        
        if(idx == k){
            if(q.empty())   // k가 움직이는 idx와 같고, 만약 큐를 다 빼면 출력을 하고 마지막이니 >를 출력한다.
                cout << num << ">" << '\n';
            else            // 인덱스는 맞으나 큐가 empty가 아니면 num을 출력한다.
                cout << num << ", ";
            
            // idx가 k인 경우 다시 0으로 초기화한다.
            idx = 0;
        }
        else{
            q.push(num);
        }
        // idx가 아직 k가 아닌 경우 num을 queue 뒤로 넘겨준다.
        // 이러한 식으로 원형 큐가 이어지는 것이다.
    }
    
    
   
    return 0;
    
}
