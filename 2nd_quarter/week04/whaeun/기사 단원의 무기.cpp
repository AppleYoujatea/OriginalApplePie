#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int divisor_cnt(int num){
    int cnt = 0;
    
    for(int i = 1; i * i <= num; i++){
        if(num % i == 0){
            if(i * i == num){
                cnt++;
            }
            else{
                cnt+= 2;
            }
        }
    }
    
    return cnt;
}

int solution(int number, int limit, int power) {
    int answer = 0;
    
    for(int i = 1; i <= number; i++){
        if(divisor_cnt(i) > limit){
            answer += power;
        }
        else{
            answer += divisor_cnt(i);
        }
    }
    
    return answer;
}
