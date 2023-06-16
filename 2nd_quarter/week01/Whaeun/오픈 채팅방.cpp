#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>

using namespace std;

// 로그 서술부 배열
string log_str[2] = {"님이 들어왔습니다.", "님이 나갔습니다."};

// 문자열 split 함수 구현
vector<string> split(string input, char delimiter) {
    vector<string> result;
    stringstream ss(input);
    string temp;
 
    while (getline(ss, temp, delimiter)){
        result.push_back(temp);
    }
 
    return result;
}


vector<string> solution(vector<string> record) {
    vector<string> answer;
    // <u_id, u_name>
    map<string, string> user_info;
    // <u_id, isEnter>
    vector<pair<string, int>> user_enter_log;
    
    for(int i = 0; i < record.size(); i++){
        vector<string> log  = split(record[i], ' ');
        
        if(log[0] == "Enter"){
            user_info[log[1]] = log[2];
            user_enter_log.push_back({log[1], 1});
        }
        else if(log[0] == "Change"){
           user_info[log[1]] = log[2];
        }
        else if(log[0] == "Leave"){
            user_enter_log.push_back({log[1], 0});
        }
    }
    
    for(int i = 0; i < user_enter_log.size(); i++){
        //Enter
        if(user_enter_log[i].second == 1){
            answer.push_back(user_info[user_enter_log[i].first] + log_str[0]);
        }
        //Leave
        else{
            answer.push_back(user_info[user_enter_log[i].first] + log_str[1]);
        }
    }
    
    return answer;
}
