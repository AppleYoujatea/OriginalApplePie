#include <string>
#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 0;
    
    int start = section[0];
    int cnt = 0;
    
    for(int i = 0; i < section.size(); i++){
        
        if(section[i] <= start && i != 0){
            continue;
        }
        else{
            cnt++;
            start = section[i] + m - 1;
        }
    }
    
    answer = cnt;
    
    
    return answer;
}
