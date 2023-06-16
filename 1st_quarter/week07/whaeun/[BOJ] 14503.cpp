#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>

using namespace std;

int mapp[55][55];
int check[55][55];

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, m, x, y, d;
    int answer = 0;
    
    cin >> n >> m >> x >> y >> d;
    
    
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            int a;
            
            cin >> a;
            
            mapp[i][j] = a;
        }
    }
    
    
    while(1){
        if (check[x][y] == false) {
            check[x][y] = true;
            answer++;
        }
                
        bool checkk = false;
        
        for (int i = 0; i < 4; i++) {
            d = (d + 3) % 4;
            
            int xx = x + dx[d];
            int yy = y + dy[d];
            
            if (mapp[xx][yy] == 0 && check[xx][yy] == false) {
                
                x += dx[d];
                y += dy[d];
                
                checkk = true;
                
                break;
            }
        }
                
        if (!checkk) {
            if (mapp[x + dx[(d + 2) % 4]][y + dy[(d + 2) % 4]] == 1){
                break;
            }
            
            x += dx[(d + 2) % 4];
            y += dy[(d + 2) % 4];
        }
    }
    
    
    cout << answer;
    
}
