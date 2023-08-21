#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int solution(int cacheSize, vector<string> cities) {
    int answer = 0;
    
    vector<string> cache;
    
    // 캐시 불가능
    if(cacheSize == 0){
        return cities.size() * 5;
    }
    
    for(int i = 0; i < cities.size(); i++){
        // 모두 소문자로 변환
        transform(cities[i].begin(), cities[i].end(), cities[i].begin(), ::tolower);
        
        auto iter = find(cache.begin(), cache.end(), cities[i]);
        
        // 캐시에 해당 글자가 없는 경우
        if(iter == cache.end()){
            //캐시가 차있을 경우
            if(cache.size() == cacheSize){
                cache.erase(cache.begin());
            }
            answer += 5;
        }
        else{
            cache.erase(iter);
            answer += 1;
        }
        
        cache.push_back(cities[i]);
    }
    
    return answer;
}
