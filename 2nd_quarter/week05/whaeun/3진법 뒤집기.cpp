#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int solution(int n) {
    int answer = 0;
    
    string str = "";
    
    while(n > 0){
        str += (n % 3 + '0');
        n /= 3;
    }
    
    reverse(str.begin(), str.end());
    
    for(int i = str.size() - 1; i >= 0; i--){
        answer += pow(3, i) * (str[i] - '0');
    }
    
    
    return answer;
}
