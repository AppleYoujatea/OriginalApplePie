#include <string>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    stack<int> num;
    
    for(int i = numbers.size() - 1; i >= 0; i--){
        
        while(!num.empty() && numbers[i] >= num.top()){
            num.pop();
        }
        
        // no bigger num
        if(num.empty()){
            answer.push_back(-1);
        }
        else{
            answer.push_back(num.top());
        }
        
        num.push(numbers[i]);
    }
    
    reverse(answer.begin(), answer.end());
    
    return answer;
}
