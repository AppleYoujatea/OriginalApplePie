#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<iomanip>

#define MAX 1000000007

using namespace std;

vector<int> v;

int main(){
    // 랜선의 길이가 2^31-1이하이기 때문에 unsigned를 붙여주어야 함
    unsigned int k, n, max_num = 0, answer = 0;
    
    cin >> k >> n;
    
    for(int i = 0; i < k; i++){
        int a;
        
        cin >> a;
        
        v.push_back(a);
        
        if(max_num < a){
            max_num = a;
        }
    }
    
    // 0으로 나누는 경우가 생기기 때문에 left를 1로 설정
    unsigned int left = 1;
    unsigned int right = max_num;
    unsigned int mid = (left + right) / 2;
    
    while(left <= right){
        mid = (left + right) / 2;
        
        unsigned int sum = 0;
        
        for(int i = 0; i < k; i++){
            sum += v[i] / mid;
        }
        
        if(sum < n){
            right = mid - 1;
        }
        else if(sum >= n){
            left = mid + 1;
            answer = max(answer, mid);
        }
    }
    
    cout << answer;
}
