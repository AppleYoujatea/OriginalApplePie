#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string new_id) {
    string answer = "";
    
    for(int i=0;i<new_id.size();i++){
        if(new_id[i] >= 'A' && new_id[i] <= 'Z')
            new_id[i] += 'a' - 'A';
    }
    
    for(int i=0;i<new_id.size();){
        if((new_id[i] >= 'a' && new_id[i] <= 'z') || (new_id[i] >= '0' && new_id[i] <= '9') || new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.'){
            i++;
            continue;       // 맞을 경우는 넘어가고
        }
        else
            new_id.erase(i, 1);   // 지워질 경우에는 다시 그 인덱스를 한다.
    }                             // 뒤의 문자가 앞으로 오므로
    // erase를 사용할 경우 해버리면 무시가 되는 i가 생길수 있으므로 다르게 한다.
    
    for(int i=0;i<new_id.size()-1;){
        if(new_id[i] == '.' && new_id[i+1] == '.'){
            new_id.erase(i, 1);
            continue;
        }
        else
            i++;        // 위의 경우와 마찬가지고 erase하면 넘어가기
    }
    
    if(new_id[0] == '.')
        new_id.erase(0,1);
    if(new_id.back() == '.')
        new_id.erase(new_id.size()-1,1);
    
    if(new_id.size() == 0)
        new_id += 'a';
    
    if(new_id.length() >= 16){
        new_id.erase(15, new_id.size() - 1);        // 이게 문제였음 (인덱스 주의)
        if(new_id[new_id.length() - 1] == '.')
            new_id.erase(new_id.size() - 1);
    }
    
    if(new_id.size() <= 2){
        while(new_id.size() != 3)
            new_id += new_id[new_id.size() - 1];
    }
    
    answer = new_id;
    
    return answer;
}
