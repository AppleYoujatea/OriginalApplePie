#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

int solution(vector<vector<string>> book_time) {
    int answer = 0;
    
    vector<int> rooms;
    
    sort(book_time.begin(), book_time.end());
    
    for(int i = 0; i < book_time.size(); i++){
        
        int hour1 = stoi(book_time[i][0].substr(0, 2));
        int minute1 = stoi(book_time[i][0].substr(3, 2));
        
        int hour2 = stoi(book_time[i][1].substr(0, 2));
        int minute2 = stoi(book_time[i][1].substr(3, 2));
        
        //분으로 시작하는 시간 계산
        int start_minute = hour1 * 60 + minute1;
        //분으로 끝나는 시간 계산
        int end_minute = hour2 * 60 + minute2;
        int check = 0;
        
        for(int j = 0; j < rooms.size(); j++){
            
            if(rooms[j] + 10 <= start_minute){
                rooms[j] = end_minute;
                check = 1;
                break;
            }
        }
        
        if(!check){
            rooms.push_back(end_minute);
        }
    }
    answer = rooms.size();
    
    return answer;
}
