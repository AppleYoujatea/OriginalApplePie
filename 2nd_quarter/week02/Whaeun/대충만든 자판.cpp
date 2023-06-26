#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> targets) {
    vector<int> answer;
    map<char, int> dic;
    
    for(int i = 0; i < keymap.size(); i++){
        for(int j = 0; j < keymap[i].size(); j++){
            if(dic[keymap[i][j]] != 0 && dic[keymap[i][j]] > j+1){
                dic[keymap[i][j]] = j + 1;
            }
            else if(dic[keymap[i][j]] == 0 ){
                dic[keymap[i][j]] = j + 1;
            }
        }
    }
    
    for(int i = 0; i < targets.size(); i++){
        int cnt = 0;
        bool check = true;
        
        for(int j = 0; j < targets[i].size(); j++){
            if(dic[targets[i][j]] == 0){
                check = false;
            }
            else{
                cnt += dic[targets[i][j]];
            }
        }
        
        if(!check){
            answer.push_back(-1);
        }
        else{
            answer.push_back(cnt);
        }
    }
    
    
    return answer;
}
