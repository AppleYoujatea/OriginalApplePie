#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};

int visited[110][110];

int bfs(int x, int y, vector<string> maps){
    int ans = 0;
    queue<pair<int, int>> q;
    
    if(visited[y][x] == 1){
        return 0;
    }
    
    q.push({x, y});
    ans += maps[y][x] - '0';
    visited[y][x] = 1;
    
    while(!q.empty()){
        int p_x = q.front().first;
        int p_y = q.front().second;
        q.pop();
        
        for(int i = 0; i < 4; i++){
            int xx = dx[i] + p_x;
            int yy = dy[i] + p_y;
            
            if(xx < 0 || yy < 0 || xx >= maps[0].size() || yy >= maps.size() || visited[yy][xx] == 1 || maps[yy][xx] == 'X'){
                continue;
            }
            
            visited[yy][xx] = 1;
            q.push({xx, yy});
            ans += maps[yy][xx] - '0';
        }
    }
    
    return ans;
}

vector<int> solution(vector<string> maps) {
    vector<int> answer;
    
    vector<pair<int, int>> island;
    
    for(int i = 0; i < maps.size(); i++){
        for(int j = 0; j < maps[0].size(); j++){
            if(maps[i][j] != 'X'){
                island.push_back({j, i});
            }
        }
    }
    
    int result = 0;
    
    for(int i = 0; i < island.size(); i++){
        result = bfs(island[i].first, island[i].second, maps);
        
        if(result != 0){
            answer.push_back(result);
        }
    }

    
    sort(answer.begin(), answer.end());
    
    if(answer.size() == 0){
        answer.push_back(-1);
    }
    
    return answer;
}
