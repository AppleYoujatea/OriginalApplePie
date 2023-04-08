#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

vector<int> visited;
vector<vector<int>>edge;
vector<int> num;

int answer = 0;

void bfs(int node){
    
    queue<int> q;
    
    q.push(node);
    visited[node] = 1;
    
    while(!q.empty()){
        int now = q.front();
        
        q.pop();
        
        for(int i = 0; i < edge[now].size(); i++){
            if(visited[edge[now][i]] == 0){
                visited[edge[now][i]] = 1;
                q.push(edge[now][i]);
            }
        }
        
        
        
    }
    
    
}

int main(){
    int n, m;
    
    cin >> n >> m;
    
    for(int i = 0;  i<=n; i++){
        edge.push_back(num);
        visited.push_back(0);
    }
    
    for(int i = 0; i < m; i++){
        int a, b;
        
        cin >> a >> b;
        
        edge[a].push_back(b);
        edge[b].push_back(a);
    }
    
    for(int i = 1; i <= n; i++){
        if(visited[i] == 0){
            bfs(i);
            answer++;
        }
    }
    
    cout << answer;
}
