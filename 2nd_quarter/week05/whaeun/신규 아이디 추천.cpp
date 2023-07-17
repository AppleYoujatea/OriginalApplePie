#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
    string answer = "";
    
    //1단계
    for(int i = 0; i < new_id.size(); i++){
        if(new_id[i] >= 'A' && new_id[i] <= 'Z'){
            new_id[i] += 32;
        }
    }
    
    string sub_str = "";
    
    //2단계
    for(int i = 0; i < new_id.size(); i++){
        if((new_id[i] >= 'a' && new_id[i] <= 'z') || (new_id[i] >= '0' && new_id[i] <= '9') || new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.' ){
            sub_str += new_id[i];
        }
    }
    
    answer += sub_str[0];
    
    //3 & 4단계
    for(int i = 1 ; i < sub_str.size(); i++){
        if(sub_str[i-1] == sub_str[i] && sub_str[i] == '.'){
            continue;
        }
        else{
            answer += sub_str[i];
        }
    }
    
    if(answer[0] == '.'){
        answer = answer.substr(1, answer.size() - 1);
    }
    
    if(answer[answer.size() - 1] == '.'){
        answer = answer.substr(0, answer.size() - 1);
    }
    
    //5단계
    if(answer == ""){
        answer += "a";
    }
    
    //6단계
    if(answer.size() >= 16){
        answer = answer.substr(0, 15);
    }
    
    if(answer[answer.size() - 1] == '.'){
        answer = answer.substr(0, answer.size() - 1);
    }
    
    //7단계
    if(answer.size() == 2){
        answer += answer[1];
    }
    
    if(answer.size() == 1){
        answer += answer[0];
        answer += answer[0];
    }
    
    return answer;
}
