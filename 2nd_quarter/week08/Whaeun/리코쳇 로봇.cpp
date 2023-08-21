#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int mapp[110][110];
int visited[110][110];
int start_x = 0, start_y = 0;
int end_x = 0, end_y = 0;

int n, m;

int answer = 1e9;

void bfs(){
    queue<pair<pair<int, int>, int>> q;
    
    q.push({{start_x, start_y}, 0});
    visited[start_x][start_y] = 1;
    
    while(!q.empty()){
        int x = q.front().first.first;
        int y = q.front().first.second;
        int cnt = q.front().second;
        
        q.pop();
        
        if(x == end_x && y == end_y){
            answer = min(answer, cnt);
        }
        
        for(int i = 0; i < 4; i++){
            int xx = x + dx[i];
            int yy = y + dy[i];
            
            if((xx < 0 || yy < 0 || xx >= n || yy >= m) || mapp[xx][yy] == 1){
                continue;
            }
            
            while(1){
                xx += dx[i];
                yy += dy[i];
                
                if((xx < 0 || yy < 0 || xx >= n || yy >= m) || mapp[xx][yy] == 1){
                    xx -= dx[i];
                    yy -= dy[i];
                    break;
                }
            }
            
            if(visited[xx][yy]){
                continue;
            }
            
            q.push({{xx, yy}, cnt + 1});
            visited[xx][yy] = 1;
        }
        
    }
}

int solution(vector<string> board) {
    n = board.size();
    m = board[0].size();
    
    for(int i = 0; i < board.size(); i++){
        for(int j = 0; j < board[0].size(); j++){
            if(board[i][j] == '.'){
                mapp[i][j] = 0;
            }
            else if(board[i][j] == 'D'){
                mapp[i][j] = 1;
            }
            else if(board[i][j] == 'R'){
                start_x = i;
                start_y = j;
                mapp[i][j] = 0;
            }
            else if(board[i][j] == 'G'){
                end_x = i;
                end_y = j;
                mapp[i][j] = 0;
            }
        }
    }
    
    bfs();
    
    if(answer == 1e9){
        return -1;
    }
    
    return answer;
}
