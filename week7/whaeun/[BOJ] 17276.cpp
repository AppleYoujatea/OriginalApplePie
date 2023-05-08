#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>

using namespace std;

int arr[510][510];
int change[510][510];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int testcase;
    
    cin >> testcase;
    
    for(int t = 0; t < testcase; t++){
        int n, d;
        
        cin >> n >> d;
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                int a;
                
                cin >> a;
                
                arr[i][j] = a;
                change[i][j] = a;
            }
        }
        
        for(int i = 0; i < abs(d/45); i++){
            int temp[510][510] = {0,};
            // 시계
            if(d > 0){
                for(int j = 0; j < n; j++){
                    temp[j][n/2] = change[j][j];
                    temp[j][j] = change[n/2][j];
                    temp[n/2][j] = change[n-j-1][j];
                    temp[n-j-1][j] = change[n-j-1][n/2];
                }
                
                for(int j = 0; j < n; j++){
                    for(int k = 0; k < n; k++){
                        change[j][k] = temp[j][k];
                    }
                }
                
            }
            // 반시계
            else{
                for(int j = 0; j < n; j++){
                    temp[j][n/2] = change[j][n-j-1];
                    temp[j][j] = change[j][n/2];
                    temp[n/2][j] = change[j][j];
                    temp[n-j-1][j] = change[n/2][j];
                }
                
                for(int j = 0; j < n; j++){
                    for(int k = 0; k < n; k++){
                        change[j][k] = temp[j][k];
                    }
                }
            }
        }
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(change[i][j] == 0){
                    change[i][j] = arr[i][j];
                }
                cout << change[i][j] << " ";
            }
            cout << "\n";
        }
    }
    
}
