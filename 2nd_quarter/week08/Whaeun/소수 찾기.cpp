#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool isPrime(int n){
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

int solution(int n) {
    int answer = 0;
    
    for(int i = 2; i  <= n; i++){
        if(isPrime(i)){
            answer++;
        }
    }
    
    return answer;
}
