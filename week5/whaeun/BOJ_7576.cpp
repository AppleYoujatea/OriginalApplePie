#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

int mapp[1010][1010];
int visited[1010][1010];

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

int answer = 0;

int main(){
    int n, m;
    int cnt = 0;
    
    cin >> n >> m;
    
    queue<pair<int, int>> q;
    
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            cin >> mapp[i][j];
            
            if(mapp[i][j] == 1){
                q.push({j, i});
                visited[i][j] = 1;
                cnt++;
            }
        }
    }
    
    q.push({-1, -1});
    
    // 처음에 모든 토마토가 익은 상태인 경우
    if(cnt == (n * m)){
        cout << 0;
        return 0;
    }
    
    // -1이 나올 경우, 일수 추가
    while(!q.empty()){
        int now_x = q.front().first;
        int now_y = q.front().second;
        
        q.pop();
        
        if(now_x == -1){
            answer++;
            if(q.empty()){
                break;
            }
            
            q.push({-1, -1});
        }
        
        for(int i = 0; i < 4; i++){
            int xx = now_x + dx[i];
            int yy = now_y + dy[i];
            
            if(xx < 0 || yy < 0 || xx >= n || yy >= m || visited[yy][xx] == 1 || mapp[yy][xx] == -1 || mapp[yy][xx] == 1){
                continue;
            }
            
            q.push({xx, yy});
            visited[yy][xx] = 1;
            
        }
        
    }
    
    // 안익은 토마토가 있는지 확인
    bool check = true;
    
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(visited[i][j] == 0 && mapp[i][j] != -1){
                check = false;
            }
        }
    }
    
    if(check){
        cout << answer - 1;
    }
    else{
        cout << -1;
    }
}
