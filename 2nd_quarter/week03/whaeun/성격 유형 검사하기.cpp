#include <string>
#include <vector>
#include <map>

using namespace std;

int score[7] = {3, 2, 1, 0, 1, 2, 3};

string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    map<char, int> character;
    
    for(int i = 0; i < survey.size(); i++){
        if(choices[i] > 4){
            character[survey[i][1]] += score[choices[i] - 1];
        }
        else if(choices[i] < 4){
            character[survey[i][0]] += score[choices[i] - 1];
        }
    }
    
    if(character['R'] >= character['T']){
        answer += 'R';
    }
    else{
        answer += 'T';
    }
    
    if(character['C'] >= character['F']){
        answer += 'C';
    }
    else{
        answer += 'F';
    }
        
     
    if(character['J'] >= character['M']){
        answer += 'J';
    }
    else{
        answer += 'M';
    }
    
    if(character['A'] >= character['N']){
        answer += 'A';
    }
    else{
        answer += 'N';
    }
    
    
    return answer;
}
