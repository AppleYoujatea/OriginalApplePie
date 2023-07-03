#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<int> food) {
    string answer = "";
    
    for(int i = 0; i < food.size(); i++){\
        for(int j = 0; j < food[i] / 2; j++){
            answer += i + '0';
        }
        
    }
    
    answer += "0";
    
    int answer_half_size = answer.size();
    
    for(int i = answer_half_size - 2; i >= 0; i--){
        answer += answer[i];
    }
    
    return answer;
}
