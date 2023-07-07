#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    map<string, int> shopping_list;
    
    for(int i = 0; i < want.size(); i++){
        shopping_list[want[i]] = number[i];
    }
    
    // 10일 모두 구매 시 answer 증가
    int days = 0;
    
    for(int i = 0; i < discount.size(); i++){
        
        if(days == 10){
            shopping_list[discount[i - 10]]++;
            days--;
        }
        
        // is exist in shopping list?
        if(shopping_list[discount[i]] > 0){
            days++;
            shopping_list[discount[i]]--;
            
            if(days == 10){
                answer++;
            }
        }
        else{
            if(days > 0){
                for(int j = days; j >= 1; j--){
                    shopping_list[discount[i - j]]++;
                    days--;
                    
                    if(shopping_list[discount[i]] > 0){
                        days++;
                        shopping_list[discount[i]]--;
            
                        break;
                    }
                }
            };
        }
    }
    
    return answer;
}
