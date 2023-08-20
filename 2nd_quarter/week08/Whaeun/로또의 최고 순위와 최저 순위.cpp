#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int arr[7] = {6, 6, 5, 4, 3, 2, 1};

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    map<int, int> win;
    
    
    sort(lottos.begin(), lottos.end());
    
    int zero_cnt = 0;
    int correct_cnt = 0;
    
    sort(win_nums.begin(), win_nums.end());
    
    for(int i = 0; i < win_nums.size(); i++){
        win[win_nums[i]]++;
    }
    
    for(int i = 0; i < lottos.size(); i++){
        if(lottos[i] == 0){
            zero_cnt++;
        }
        else if(win[lottos[i]] > 0){
            correct_cnt++;
        }
    }
    answer.push_back(arr[zero_cnt + correct_cnt]);
    answer.push_back(arr[correct_cnt]);
    
    return answer;
}
