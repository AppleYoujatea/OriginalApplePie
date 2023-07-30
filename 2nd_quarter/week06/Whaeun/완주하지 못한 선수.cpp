#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    map<string, int> check;
    map<string, int> parti;
    
    for(int i = 0; i < completion.size(); i++){
        check[completion[i]]++;
    }
    
    for(int i = 0; i < participant.size(); i++){
        parti[participant[i]]++;
    }
    
    for (auto iter = parti.begin(); iter != parti.end(); ++iter) {
        
        for(int i = 0; i < parti[iter->first] - check[iter->first]; i++){
            answer = iter -> first;
        }
    }
    
    return answer;
}
