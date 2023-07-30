#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    vector<int> arr;
    
    
    for(int i = 0; i < n; i++){
        arr.push_back(arr1[i] | arr2[i]);
    }
    
    string s;
    
    for(int j = 0; j < n; j++){
        for (int i = n-1; i >= 0; i--){
            int temp = (arr[j] >> i) & 1;
            if(temp == 0){
                s += " ";
            }
            else{
                s += "#";
            }
        }

        answer.push_back(s);
        s = "";
    }
    
    return answer;
}
