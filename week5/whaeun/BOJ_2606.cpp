#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

vector<vector<int>> edge;
vector<int> num;
vector<int> visited;

int answer = 0;

void dfs(int node){
    cout << node << " ";
    visited[node] = true;
    
    for(int i = 0; i < edge[node].size(); i++){
        int next = edge[node][i];
        
        if(!visited[next]){
            visited[next] = true;
            dfs(next);
        }
    }
}

void bfs(int node){
    queue<int> q;
    
    q.push(node);
    visited[node] = true;
    
    while(!q.empty()){
        int now = q.front();
        answer++;
        q.pop();
        
        for(int i = 0;  i < edge[now].size(); i++){
            if(!visited[edge[now][i]]){
                q.push(edge[now][i]);
                visited[edge[now][i]] = true;
            }
            
            
        }
        
    }
}


int main(){
    
    int n, m;
    
    cin >> n >> m;
    
    for(int i = 0; i <= n; i++){
        edge.push_back(num);
        visited.push_back(0);
    }
    
    for(int i = 0; i < m; i++){
        int a, b;
        
        cin >> a >> b;
        
        edge[a].push_back(b);
        edge[b].push_back(a);
    }
    
    for(int i = 0; i <= n; i++){
        sort(edge[i].begin(), edge[i].end());
    }
    
    bfs(1);
    
    cout << answer - 1;
}

