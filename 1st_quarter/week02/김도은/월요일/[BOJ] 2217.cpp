#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>

using namespace std;

int main(){
    
    int n;
    
    cin >> n;
    
    vector<int> rope;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        rope.push_back(a);
        
    }
    
    sort(rope.begin(), rope.end(), greater<>());
    
    int max = rope[0];
    
    for(int i = 1; i < n; i++){
        int weight = rope[i] * (i+1);
        
        if(weight > max){
            max = weight;
        }
    }
    
    cout << max;
    
}
