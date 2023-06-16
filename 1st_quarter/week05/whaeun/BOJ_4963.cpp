#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

int mapp[55][55];
int visited[55][55];

int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[8] = {1, 0, -1, 1, -1, 1, 0, -1};

int w, h;

void bfs(int x, int y){
    
    queue<pair<int, int>> q;
    
    q.push({x, y});
    
    while(!q.empty()){
        int now_x = q.front().first;
        int now_y = q.front().second;
        
        q.pop();
        
        for(int i = 0; i < 8; i++){
            int xx = now_x + dx[i];
            int yy = now_y + dy[i];
            
            if(yy < 0 || xx < 0 || yy >= h || xx >= w || mapp[yy][xx] == 0 || visited[yy][xx] == 1){
                continue;
            }
            
            visited[yy][xx] = 1;
            q.push({xx, yy});
            
        }
        
        
        
        
        
    }
    
    
}

int main(){
    int answer;
    
    cin >>  w >> h;
    
    while (!(w == 0 && h == 0)) {
        answer = 0;
        
        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                cin >> mapp[i][j];
            }
        }
        
        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                visited[i][j] = 0;
            }
        }
        
        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                if(visited[i][j] == 0 && mapp[i][j] == 1){
                    bfs(j, i);
                    answer++;
                }
            }
        }
        
        cout << answer << "\n";
        
        cin >> w >> h;
    }
}
