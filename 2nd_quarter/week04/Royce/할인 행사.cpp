#include <string>
#include <vector>
#include <map>
#include <unordered_map>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    
    unordered_map<string, int> mp;
    for(int i=0;i<number.size();i++)
        mp.insert({want[i], number[i]});
    // mp[want[i]] = number[i]와 같은 의미인듯
    
    // i에 대하여 +10을 해주어야 하므로 범위는 전체-10으로 한다.
    for(int i=0;i<=discount.size() - 10;i++){
        unordered_map<string, int>mp2;
        for(int j=i;j<i+10;j++){
            mp2[discount[j]] += 1;
        }
        // mp2에 경우에도 i ~ i+10 까지 비교해주며 매번 map을 만들어 수를 세준다.
        if(mp2 == mp)
            answer++;
        // 이때 mp와 mp2가 같은 경우 answer를 늘려준다.
        
        // ** 시작하는 날짜가 아닌 모두 할인 받을 수 있는 날짜의 총 일수를 출력하는 것 이므로
        // 각각 answer++ 해주어야 한다. **
    }
    
    
    
    return answer;
}
