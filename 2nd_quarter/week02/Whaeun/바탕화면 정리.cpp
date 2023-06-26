#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    vector<int> answer;
    
    int min_left = 55, max_right = 0, min_bottom = 55, max_top = 0;
    
    for(int i = 0; i < wallpaper.size(); i++){
        for(int j = 0; j < wallpaper[i].size(); j++){
            if(wallpaper[i][j] == '#'){
                if(min_left > j){
                    min_left = j;
                }
                
                if(min_bottom  > i){
                    min_bottom = i;
                }
                
                if(max_right < j+1){
                    max_right = j+1;
                }
                
                if(max_top < i+1){
                    max_top = i+1;
                }
            }
        }
    }
    
    answer.push_back(min_bottom);
    answer.push_back(min_left);
    
    
    
    answer.push_back(max_top);
    answer.push_back(max_right);
    
    return answer;
}
