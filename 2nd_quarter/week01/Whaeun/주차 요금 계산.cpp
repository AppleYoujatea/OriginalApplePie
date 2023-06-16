#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;

// calculate parking time
int parkingTime(string in, string out) {
    
    int hour1 = stoi(in.substr(0, 2));
    int minute1 = stoi(in.substr(3, 2));
    int hour2 = stoi(out.substr(0, 2));
    int minute2 = stoi(out.substr(3, 2));
    
    // calculate as minute
    int parking_time = (hour2-hour1)*60 + (minute2-minute1);
    
    return parking_time;
}


vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    vector<pair<int, int>> num_answer;
    
    map<string, vector<string>> record;
    
    stringstream ss;
    
    for(int i = 0; i < records.size(); i++){
        string time, num, status; 
        
        ss.str(records[i]);
        
        ss >> time >> num >> status;
        
        //mapping time with car_num
        record[num].push_back(time);
        
        ss.clear();
        
    }
    
    for(auto iter: record) {
        
        // doesn't have leaving time
        if(iter.second.size() % 2 == 1){
            iter.second.push_back("23:59");
        }
        
        
        int sum = 0;
        
        // calculate each parking fee
        for(int i = 0; i < iter.second.size() - 1; i += 2) {
            sum += parkingTime(iter.second[i], iter.second[i+1]);
        }
        
        // basic fee
        int price = fees[1];
        
        // over basic fee 
        if(sum > fees[0]) {
            price += ceil((double)(sum-fees[0]) / (double)fees[2]) * fees[3];
        }
        
        answer.push_back(price);
    }
    
    return answer;
}
