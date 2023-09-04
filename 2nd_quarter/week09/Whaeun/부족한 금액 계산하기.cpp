#include <iostream>
#include <map>
#include <algorithm>


using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = 0;
    answer = money;
    
    for(int i = 1; i <= count; i++){
           answer -= (price *i);
    }
    
    if(answer > 0){
        answer = 0;
    }
    else{
        answer *= -1;
    }

    return answer;
}
