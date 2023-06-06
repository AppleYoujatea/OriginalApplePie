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



bool col[31];
bool check_left[31];
bool check_right[31];
int num = 0;

void DFS(int level){
    
    if(level == n){
        num++;
        return;
    }
    
    // check_left는 왼쪽 위 대각선을 나타내고, x,y의 합이 같다는 성질을 가진다.
    // 따라서 left에서는 합이 같으면 된다.
    
    // check_right는 오른쪽 아래 대각선을 나타내고,
    // x - y의 값이 모두 같다는 특징을 생각한다.
    // 이때 음수가 나올 수가 있으므로 30칸 정도를 논다.
    
    for(int i=0;i<n;i++){
        if(col[i] || check_left[level - i + n-1] || check_right[i + level])
            continue;
        
        // 일단 처음으로 arr[i]는 같은 열에 존재하는 지를 확인한다.
        // right는 우측 상단 대각선에 left는 좌상단에 위치하는지 확인
        
        // right에서는 i에 해당하는 숫자에서 level 만큼을 더해주고,
        // left에서는 level-i+n-1 즉, right와 더해서 n-1이 나오게 해준다.
        
        // 위 중 하나라도 true면 안되서 그냥 넘어가고 다 false일 경우 밑을 true로 하고 DFS를 한다.
        
        col[i] = true;
        check_right[i + level] = true;
        check_left[level - i + n - 1] = true;
        DFS(level + 1);
        
        // DFS에서 성공을 하고 num을 증가시키면 하나 전으로 돌아가서 false를 만들고
        // i를 늘리고 다시 찾아가는 것이 백트래킹의 중요 포인트이다.
        // 여기서 모든 for문에 대해 시도하고 없다면 또 한번 DFS를 나와서 n-2번째로 간다.
        
        col[i] = false;
        check_right[i + level] = false;
        check_left[level - i + n - 1] = false;
        
        // 퀸의 위치를 true로 표시한다.
    }
    
    
    
    
}





int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    cin >> n;
    
    DFS(0);
    
    cout << num;
    
    
    
    return 0;
    
}

// 0 X X X
// X X X
// X   X
// X     X

// 이므로 다음 열을 탐색할 경우에 3번째인 곳에 퀸이 들어갈 수 있다.
// 이때 따라서 퀸을 넣어주고 다시 여기서 또 탐색한다.


