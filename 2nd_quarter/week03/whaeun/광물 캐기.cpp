#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int solution(vector<int> picks, vector<string> minerals) {
    int answer = 0;
    
    vector<int> mine;
    
    vector<pair<int,int>> mine_sum;
    vector<pair<int,int>> picks_order;
    
    int dia = picks[0];
    int iron = picks[1];
    int stone = picks[2];
    
    int sum = 0;
    
    for(int i = 0; i < minerals.size(); i++){
        if(minerals[i] == "diamond"){
            mine.push_back(3);
        }
        else if(minerals[i] == "iron"){
            mine.push_back(2);
        }
        else{
            mine.push_back(1);
        }
        
        sum += pow(5, mine[i] - 1);
        
        if(i % 5 == 4){
            mine_sum.push_back({sum, i / 5});
            sum = 0;
        }
        
    }
    
    if(sum != 0){
        mine_sum.push_back({sum, minerals.size() / 5});
    }
    
    sort(mine_sum.begin(), mine_sum.end());
    
    for(int i = mine_sum.size() - 1; i >= 0; i--){
        if(dia > 0){
            picks_order.push_back({mine_sum[i].second, 3});
            dia -= 1;
            continue;
        }
        
        if(iron > 0){
            picks_order.push_back({mine_sum[i].second, 2});
            iron -= 1;
            continue;
        }
        
        if(stone > 0){
            picks_order.push_back({mine_sum[i].second, 1});
            stone -= 1;
            continue;
        }
    }
    
    sort(picks_order.begin(), picks_order.end());
    
    int idx = 0;
    
    for(int i = 0; i < min(mine.size(), picks_order.size() * 5); i++){
        if(picks_order[idx].second >= mine[i]){
            answer += 1;
        }
        else{
            answer += pow(5,  mine[i] - picks_order[idx].second);
        }
        
        if(i % 5 == 4){
            idx++;
        }
    }
    
    return answer;
}
