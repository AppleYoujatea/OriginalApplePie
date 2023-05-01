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
#define mod1 1000000000
#define mod 1000000007
#define pii pair<int, int>
using ll = long long;
using namespace std;
int n,m,k;
int l,r,t;
int h;


string st;

int palin(int left, int right, bool check){
    while(left < right){
        if(st[left] != st[right]){
            if(check){
                if(palin(left + 1, right, false) == 0 || palin(left, right-1, false) == 0)
                    return 1;
                // left나 right를 좁히면서 st[left], st[right]가 모두 같은 경우 한개만 다르므로 유사회문
            }
            return 2;
            // 다른 경우가 있을 경우 안되므로 2
        }
        left++;
        right--;
    }
    return 0;
}


int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    // 회문 : 앞뒤로 같은 것
    // 유사회문 : 그 자체는 아니지만 한 문자를 삭제하여 회문으로 만들 수 있으면 유사회문
    cin >> t;
    
    for(int i=0;i<t;i++){
        cin >> st;
        
        cout << palin(0, st.length()-1, true) << '\n';
        
    }
    
    
    
    
    return 0;
    
}
