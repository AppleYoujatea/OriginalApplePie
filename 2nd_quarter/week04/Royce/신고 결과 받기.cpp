#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <set>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    vector<int> answer(id_list.size(), 0);
    // 개수를 0으로 할당해준다.
    
    map<string, int> mp;
    map<string, set<string>> mp_report;
    // 신고한 아이디를 중복을 없애줘야하므로 set으로 처리한다.
    
    for(int i=0;i<id_list.size();i++){
        mp[id_list[i]] = i;
        // 각각의 스트링에 번호를 부여한다.
    }
    
    for(auto re : report){
        stringstream ss(re);
        string a, b;
        ss >> a >> b;
        
        mp_report[b].insert(a);
        // a가 b를 신고하였으므로, b에 a를 넣어줌
        // [신고당한 id, 신고한 id]
    }
    
    for(auto re : mp_report){
        if(re.second.size() >= k){   // k.second는 신고당한 사람에 관해 신고한 사람의 수
            for(auto ch : re.second){   // 즉 second일 경우 신고한 사람들이므로
                answer[mp[ch]]++;       // 그에 관하여 메일을 다 보내주었다.
            }
            // 위에서 mp[ch]에 관해서 번호를 할당해야 answer에서 그에 알맞은 인덱스에 추가됨
        }
    }
    
    
    return answer;
}

