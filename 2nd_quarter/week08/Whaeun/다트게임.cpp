#include <string>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int solution(string dartResult) {
    int answer = 0;
    int idx = 0;
    
    vector<int> score;
    
    for(int i = 0; i < dartResult.size(); i++){
        //10인 경우
        if(dartResult[i] >= '0' && dartResult[i] <= '9' && dartResult[i+1] >= '0' && dartResult[i+1] <= '9'){
            score.push_back(10);
            i++;
        }
        // 0 ~ 9인 경우
        else if(dartResult[i] >= '0' && dartResult[i] <= '9'){
            score.push_back(dartResult[i] - '0');
        }
        else{
            if(dartResult[i] == 'D'){
                score[score.size()-1] = pow(score[score.size()-1], 2);
            }
            else if(dartResult[i] == 'T'){
                score[score.size()-1] = pow(score[score.size()-1], 3);
            }
            else if(dartResult[i] == '*'){
                score[score.size()-1] *= 2;
                score[score.size()-2] *= 2;
            }
            else if(dartResult[i] == '#'){
                score[score.size()-1] *= -1;
            }
            
        }
    }
    
    for(int i = 0; i < score.size(); i++){
        answer += score[i];
    }
    
    return answer;
}
