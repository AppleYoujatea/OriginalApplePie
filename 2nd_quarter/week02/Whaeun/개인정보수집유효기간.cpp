#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;

// calculate store time
int storeTime(string in, string out) {
    
    int year1 = stoi(in.substr(0, 4));
    int month1 = stoi(in.substr(5, 2));
    
    int year2 = stoi(out.substr(0, 4));
    int month2 = stoi(out.substr(5, 2));
    
    // calculate time
    // month_diff가 같을 경우, day가 다른지 확인해야 함
    int month_diff = (year1 - year2) * 12 + (month1 - month2);
    
    return month_diff;
}



vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
    map<char, int> dic;
    
    
    for(int i = 0; i < terms.size(); i++){
        if(terms[i].size() == 4) {
            dic[terms[i][0]] = stoi(terms[i].substr(2, 2));
        }
        else if(terms[i].size() == 3) {
            dic[terms[i][0]] = stoi(terms[i].substr(2, 1));
        }
        else{
            dic[terms[i][0]] = stoi(terms[i].substr(2, 3));
        }
    }
    
    
    for(int i = 0; i < privacies.size(); i++){
        string date, type; 
        stringstream ss;
        
        ss.str(privacies[i]);
        
        ss >> date >> type;
        
        int month_diff = storeTime(today, date);
        
        // 파기해야 하는 경우
        if(month_diff > dic[type[0]]){
            answer.push_back(i+1);;
        }
        else if(month_diff == dic[type[0]]){
            // 일자 비교 필요
            int day1 = stoi(today.substr(8, 2));
            int day2 = stoi(date.substr(8, 2));
            
            if(day1 >= day2){
                answer.push_back(i+1);;
            }
        }
    }
    
    return answer;
}
