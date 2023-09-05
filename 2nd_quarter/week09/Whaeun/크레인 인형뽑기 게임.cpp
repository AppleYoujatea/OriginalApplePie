#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> stack;

    for (int i= 0; i < moves.size(); i++){
        int target = moves[i];
        
        int findNum =0;
    
        for(int i=0; i < board[target - 1].size(); i++){

            if (0 != board[i][target - 1]) {
                findNum = board[i][target - 1];            
                board[i][target - 1] = 0;
                break;
            }
        }
        
        
        if (0 != findNum){
            
            bool sameCheck = false;
            if (0 != stack.size()){
                int temp = stack[stack.size()-1];

                if(findNum == temp){
                    sameCheck = true;
                }
            }
            if (false == sameCheck){                
                stack.push_back(findNum);
            }
            else{
                answer += 2;
                stack.pop_back();
            }
            
        }
        
        
    }
    
    return answer;
}
