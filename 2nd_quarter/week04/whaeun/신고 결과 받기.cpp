#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer;
    
    map<string, int> cnt;
    map<string, int> name_idx;
    
    vector<string> report_list[1010];
    
    sort(report.begin(), report.end());
    report.erase(unique(report.begin(), report.end()), report.end());
    
    for(int i = 0; i < id_list.size(); i++){
        name_idx.insert({id_list[i], i});
    }
    
    bool space = false;
    
    for (int i = 0; i < report.size(); i++){
        string user_id, report_id;
        
        stringstream ss(report[i]);
        
        ss >> user_id >> report_id;
        
        report_list[name_idx[user_id]].push_back(report_id);
        cnt[report_id]++;
    }
    
     for (int i = 0; i < id_list.size(); i++){
        int mail_cnt = 0;
         
        for (int j = 0; j < report_list[i].size(); j++){
            if (cnt[report_list[i][j]] >= k){
                mail_cnt++;
            }
            
        }
         
        answer.push_back(mail_cnt);
    }
    
    return answer;
}
