#include <string>
#include <vector>

using namespace std;
    
char arr[55][55];

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1,1, 0, 0};

vector<int> solution(vector<string> park, vector<string> routes) {
    vector<int> answer;
    
    int pos_x = 0, pos_y = 0;
    
    int width = park[0].size();
    int height = park.size();
    
    for(int i = 0; i < park.size(); i++){
        for(int j = 0; j < park[i].size(); j++){
            arr[i][j] = park[i][j];
            
            if(park[i][j] == 'S'){
                pos_x = j;
                pos_y = i;
            }
        }
    }
    
    for(int i = 0; i < routes.size(); i++){
        int origin_x = pos_x;
        int origin_y = pos_y;
        
        if(routes[i][0] == 'N'){
            for(int j = 0; j < routes[i][2] - '0'; j++){
                pos_x += dx[0];
                pos_y += dy[0];
                
                if(arr[pos_y][pos_x] == 'X' || pos_y < 0 || pos_x < 0 || pos_y >= height || pos_x >= width){
                    pos_x = origin_x;
                    pos_y = origin_y;
                    break;
                }
            }
        }
        else if(routes[i][0] == 'S'){
            for(int j = 0; j < routes[i][2] - '0'; j++){
                pos_x += dx[1];
                pos_y += dy[1];
                
                if(arr[pos_y][pos_x] == 'X' || pos_y < 0 || pos_x < 0 || pos_y >= height || pos_x >= width){
                    pos_x = origin_x;
                    pos_y = origin_y;
                    break;
                }
            }
        }
        else if(routes[i][0] == 'W'){
            for(int j = 0; j < routes[i][2] - '0'; j++){
                pos_x += dx[2];
                pos_y += dy[2];
                
                if(arr[pos_y][pos_x] == 'X' || pos_y < 0 || pos_x < 0 || pos_y >= height || pos_x >= width){
                    pos_x = origin_x;
                    pos_y = origin_y;
                    break;
                }
            }
        }
        else if(routes[i][0] == 'E'){
            for(int j = 0; j < routes[i][2] - '0'; j++){
                pos_x += dx[3];
                pos_y += dy[3];
                
                if(arr[pos_y][pos_x] == 'X' || pos_y < 0 || pos_x < 0 || pos_y >= height || pos_x >= width){
                    pos_x = origin_x;
                    pos_y = origin_y;
                    break;
                }
            }
        }
        
    }
    
    answer.push_back(pos_y);
    answer.push_back(pos_x);
    
    
    return answer;
}
