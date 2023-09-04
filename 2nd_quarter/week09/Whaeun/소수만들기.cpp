#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool prime[3010];

int solution(vector<int> nums) {
    int answer = 0;
    
    for(int i = 0; i< 3010; i++){
        prime[i] = true;
    }

    prime[0] = false;
    prime[1] = false;
    
    for(int i=4; i<=3000; i++){
        for(int j=2; j*j <= i; j++){
            if (i % j == 0) {
                prime[i] = false;
                break;
            }
        }
    }
    
    for(int i = 0; i < nums.size(); i++){
        for(int j = i+1; j < nums.size(); j++){
            for(int k = j+1; k < nums.size(); k++){
                if(prime[nums[i] + nums[j] + nums[k]]){
                    answer += 1;
                }
            }
        }
    }
    

    return answer;
}
