#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    
    map<int, int> extra;
    
    answer = n - lost.size();
    
    for(int i = 0; i < reserve.size(); i++){
        extra[reserve[i]] = 1;
    }
    
    sort(lost.begin(), lost.end());
    
    for(int i = 0; i < lost.size(); i++){
        if(extra[lost[i]] != 0){
            extra[lost[i]] = 0;
            lost[i] = -1;
            answer++;
        }
    }
    
    for(int i = 0; i < lost.size(); i++){
        
        if(lost[i] == -1){
            continue;
        }
        
        if(lost[i] > 1 && extra[lost[i] - 1] != 0){
            extra[lost[i]-1] = 0;
            answer++;
        }
        else if(lost[i] + 1 <= n && extra[lost[i] + 1] != 0){
            extra[lost[i]+1] = 0;
            answer++;
        }
    }
    
    return answer;
}
