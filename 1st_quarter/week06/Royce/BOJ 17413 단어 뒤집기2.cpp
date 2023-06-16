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


string st[501];

void rev(stack<char> &s){
    while(!s.empty()){
        cout << s.top();
        s.pop();
    }
}



int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    string st;
    getline(cin, st);
    // 한줄 자체를 받는다.
    
    bool check = false;
    stack<char>s;
    
    for(char c: st){
        if(c == '<'){   // c가 <일 경우 안의 단어들을 넣어주고 뒤집어준다.
            rev(s);
            check = true;
            cout << c;
        }
        else if(c == '>'){  // c가 >일 경우에 >인 c만 출력해준다. check는 다시 false로
            check = false;
            cout << c;
        }
        else if(c == ' '){  // 공백인 경우 다시 뒤집어준다.
            rev(s);
            cout << c;
        }
        else if(check){    // 아직 <이므로 출력해준다.
            cout << c;
        }
        else{
            s.push(c);
        }
    }
        
    rev(s);
    cout << '\n';
    
    
    return 0;
    
}
