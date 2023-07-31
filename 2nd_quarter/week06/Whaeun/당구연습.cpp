#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

vector<int> solution(int m, int n, int startX, int startY, vector<vector<int>> balls) {
    vector<int> answer;
    
    for(int i = 0; i < balls.size(); i++){
        int k = 100000000;
        
        if (startX != balls[i][0] || balls[i][1] > startY){
            if( k > pow((startX - balls[i][0]), 2) + pow((startY + balls[i][1]), 2)){
                k = pow((startX - balls[i][0]), 2) + pow((startY + balls[i][1]), 2);
            }
        }
        if(startY != balls[i][1] || balls[i][0] > startX){
            if( k > pow((startX + balls[i][0]), 2) + pow((startY - balls[i][1]), 2)){
                k = pow((startX + balls[i][0]), 2) + pow((startY - balls[i][1]), 2);
            }
        }
        if(startX != balls[i][0] || balls[i][1] < startY){
            if( k > pow((startX - balls[i][0]), 2) + pow((2 * n - balls[i][1] - startY), 2)){
                k = pow((startX - balls[i][0]), 2) + pow((2 * n - balls[i][1] - startY), 2);
            }
        }
        if(startY != balls[i][1] || balls[i][0] < startX){
            if( k > pow((2 * m - balls[i][0] - startX), 2) + pow((startY-balls[i][1]), 2)){
                k = pow((2 * m - balls[i][0] - startX), 2) + pow((startY-balls[i][1]), 2);
            }
        }
            
        answer.push_back(k);
            
    }
                    
    
    return answer;
}
