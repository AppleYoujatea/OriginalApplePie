#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    
    stack<int>st;
    
    for(int i=0;i<moves.size();i++){
        int num = moves[i] - 1;
        for(int j=0;j<board.size();j++){
            if(board[j][num]){
                if(!st.empty() && st.top() == board[j][num]){
                    st.pop();
                    answer += 2;
                }
                else
                    st.push(board[j][num]);
                board[j][num] = 0;
                break;
                // 0으로 만들고 break 시키고 다음 i를 진행한다.
            }
        }
    }
    
    return answer;
}

// 00000
// 00103
// 02501
// 42442
// 35131

// 1 5 3 5 1 2 1 4
