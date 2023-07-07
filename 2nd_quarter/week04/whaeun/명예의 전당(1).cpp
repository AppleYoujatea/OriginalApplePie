#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int k, vector<int> score) {
    vector<int> answer;
    vector<int> v;
    
    for(int i = 0 ; i < score.size(); i++){
        v.push_back(score[i]);
        
        sort(v.begin(), v.end());
        if(i < k){
            answer.push_back(v[0]);
        }
        else{
            answer.push_back(v[v.size() - k]);
        }
    }
    
    return answer;
}
