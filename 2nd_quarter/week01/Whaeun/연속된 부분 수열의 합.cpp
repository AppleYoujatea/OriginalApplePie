#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;
    
    int start = 0, end = 0;
    int ans_start = 0, ans_end = 0;
    int sum = sequence[0];
    
    while(start <= end){
        // compare sum with k
        if(sum < k){
            if(end + 1 >= sequence.size()){
                break;
            }
            end++;
            sum += sequence[end];
        }
        else if(sum > k){
            
            if(start + 1 >= sequence.size()){
                break;
            }
            sum -= sequence[start];
            start++;
        }
        else{
            // check answer
            if(ans_start == 0 && ans_end == 0){
                ans_start = start;
                ans_end = end;
            }
            else{
                // compare length
                if(ans_end - ans_start > end - start){
                    ans_start = start;
                    ans_end = end;
                }
            }
            
            if(start + 1 >= sequence.size()){
                break;
            }
            sum -= sequence[start];
            start++;
            
        }
        
        
    }
    
    // answer section
    answer.push_back(ans_start);
    answer.push_back(ans_end);
    
    return answer;
}
