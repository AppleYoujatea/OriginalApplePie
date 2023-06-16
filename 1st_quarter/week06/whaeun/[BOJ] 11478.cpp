#include <iostream>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

int main(){
    string str, str2;
    
    cin >> str;
    
    map<string, int> dic;
    
    for(int i = 0; i <= str.length(); i++){
        
        for(int j = 0; j <= str.length(); j++){
            str2 = str.substr(i, j);
            dic[str2]++;
        }
    }
    
    cout << dic.size() - 1;
    
}
