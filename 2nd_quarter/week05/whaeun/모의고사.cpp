#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int arr1 [5] = {1, 2, 3, 4, 5};
int arr2 [8] = {2, 1, 2, 3, 2, 4, 2, 5};
int arr3 [10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    int score1 = 0, score2 = 0, score3 = 0;
    
    for(int i = 0; i < answers.size(); i++){
        if(arr1[i % 5] == answers[i]){
            score1++;
        }
    }
    
    for(int i = 0; i < answers.size(); i++){
        if(arr2[i % 8] == answers[i]){
            score2++;
        }
    }
    
    for(int i = 0; i < answers.size(); i++){
        if(arr3[i % 10] == answers[i]){
            score3++;
        }
    }
    
    vector<pair<int, int>> v;
    
    v.push_back({score1, 1});
    v.push_back({score2, 2});
    v.push_back({score3, 3});
    
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    
    if(v[0].first > v[1].first){
        answer.push_back(v[0].second);
    }
    else if (v[0].first == v[1].first && v[1].first == v[2].first){
        answer.push_back(v[0].second);
        answer.push_back(v[1].second);
        answer.push_back(v[2].second);
    }
    else{
        answer.push_back(v[0].second);
        answer.push_back(v[1].second);
    }
    
    sort(answer.begin(), answer.end());
    
    return answer;
}
