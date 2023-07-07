#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, int m, vector<int> score) {
    int answer = 0;
    
    sort(score.begin(), score.end());
    
    for(int i = score.size() - 1; i >= 0;i -= m){
        if(i-(m-1) >= 0){
            answer += score[i-(m-1)] * m;
        }
    }
    
    return answer;
}
