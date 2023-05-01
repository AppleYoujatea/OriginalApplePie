#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main(){
    int n, m;
    vector<string> answer;
    
    cin >> n >> m;
    
    map<string, int> dic;
    
    for(int i = 0; i < n; i++){
        string str;
        
        cin >> str;
        
        dic[str]++;
    }
    
    for(int j = 0; j < m; j++){
        string str;
        
        cin >> str;
        
        dic[str]++;
    }
    
    for (auto iter : dic) {
        if(iter.second == 2){
            answer.push_back(iter.first);
        }
    }
    
    cout << answer.size() << "\n";
    
    for(int i = 0; i < answer.size(); i++){
        cout << answer[i] << "\n";
    }
    
    
}

