#include <string>
#include <vector>
#include <stack>

using namespace std;

int arr[4] = {1, 2, 3, 1};


int solution(vector<int> ingredient) {
    int answer = 0;
    string str = "";
    
    for(int i = 0; i < ingredient.size(); i++){
        str += '0' + ingredient[i];
    }
    
    int pos = 0;
    
    while (true) {
        int position = str.find("1231", pos);
        
        if (position == -1){
            break;
        }
        
        str.erase(position, 4);
        
        if (position > 2){
            pos = position - 3;
        }
            
        answer++;
    }
    
    return answer;
}
