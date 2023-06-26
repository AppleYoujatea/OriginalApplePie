#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

int dist[110][110];
int mapp[110][110];

int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};

int start_x = 0, start_y = 0;
int end_x = 0, end_y = 0;
int lever_x = 0, lever_y = 0;

int n, m;

void bfs(int start_xx, int start_yy){
    queue<pair<int, int>> q;
    
    q.push({start_xx, start_yy});
    
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        
        q.pop();
        
        for(int i = 0; i < 4; i++){
            int xx = x + dx[i];
            int yy = y + dy[i];
            
            if(xx < 0 || yy < 0 || xx >= n || yy >= m || mapp[yy][xx] == 0){
                continue;
            }
            
            if(dist[yy][xx] > dist[y][x] + 1){
                dist[yy][xx] = dist[y][x] + 1;
                q.push({xx, yy});
            }
            
        }
    }
    
}

int solution(vector<string> maps) {
    int answer = 0;
    
    n = maps[0].size();
    m = maps.size();
    
    for(int i = 0; i < 110; i++){
        for(int j = 0; j < 110; j++){
            dist[i][j] = 1e9;
        }
    }
    
    for(int i = 0; i < maps.size(); i++){
        for(int j = 0; j < maps[i].size(); j++){
            
            if(maps[i][j] == 'S'){
                start_x = j;
                start_y = i;
                
                mapp[i][j] = 1;
                dist[i][j] = 0;
            }
            else if(maps[i][j] == 'E'){
                end_x = j;
                end_y = i;
                
                mapp[i][j] = 1;
            }
            else if(maps[i][j] == 'L'){
                lever_x = j;
                lever_y = i;
                
                mapp[i][j] = 1;
            }
            else if(maps[i][j] == 'O'){
                mapp[i][j] = 1;
            }
            else{
                mapp[i][j] = 0;
            }
        }
    }
    
    bfs(start_x, start_y);
    
    if(dist[lever_y][lever_x] == 1e9){
        return -1;
    }
    else{
        answer += dist[lever_y][lever_x];
    }
    
    for(int i = 0; i < 110; i++){
        for(int j = 0; j < 110; j++){
            dist[i][j] = 1e9;
        }
    }
    
    dist[lever_y][lever_x] = 0;
    
    bfs(lever_x, lever_y);
    
    if(dist[end_y][end_x] == 1e9 ){
        answer = -1;
    }
    else{
        answer += dist[end_y][end_x];
    }
    
    return answer;
}
