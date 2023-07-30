#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string X, string Y) {
    string answer = "";
    
    
    int idx1 = 0, idx2 = 0;
    
    sort(X.begin(), X.end());
    sort(Y.begin(), Y.end());
    
    while(idx1 < X.size() && idx2 < Y.size()){
        if(X[idx1] == Y[idx2]){
            answer += X[idx1];
            idx1++;
            idx2++;
        }
        else if(X[idx1] > Y[idx2]){
            idx2++;
        }
        else{
            idx1++;
        }
        
    }
    
    if(answer == ""){
        return "-1";
    }
    
    sort(answer.begin(), answer.end(), greater<>());
    
    if(answer[0] == '0'){
        answer = "0";
    }
    
    return answer;
}
