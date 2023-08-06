#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

long long solution(int r1, int r2) {
    long long answer = 0;
    
    answer += (r2 - r1 + 1) * 4;
    
    for(int i = 1; i < r2; i++){
        long long y1 = ceil(sqrt(pow(r1, 2) - pow(i, 2)));
        long long y2 = sqrt(pow(r2, 2) - pow(i, 2));
        
        answer += (y2 - y1) * 4;
            
        if(i < r1 && (long long)sqrt(pow(r1, 2) - pow(i, 2)) % 1 == 0){
            answer += 4;
        }
    }
    
    return answer;
}
