#include <string>
#include <vector>

using namespace std;

string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    
    int rion = 0, tube = 0, con = 0, frodo = 0, jayz = 0, muzi = 0;
    int apeach = 0, neo = 0;
    for(int i=0;i<survey.size();i++){
        
        if(survey[i] == "RT"){
            if(choices[i] == 1)
                rion += 3;
            else if(choices[i] == 2)
                rion += 2;
            else if(choices[i] == 3)
                rion += 1;
            else if(choices[i] == 5)
                tube += 1;
            else if(choices[i] == 6)
                tube += 2;
            else if(choices[i] == 7)
                tube += 3;
        } // 1
        
        if(survey[i] == "TR"){
            if(choices[i] == 1)
                tube += 3;
            else if(choices[i] == 2)
                tube += 2;
            else if(choices[i] == 3)
                tube += 1;
            else if(choices[i] == 5)
                rion += 1;
            else if(choices[i] == 6)
                rion += 2;
            else if(choices[i] == 7)
                rion += 3;
        }  // 2
        
        if(survey[i] == "FC"){
            if(choices[i] == 1)
                frodo += 3;
            else if(choices[i] == 2)
                frodo += 2;
            else if(choices[i] == 3)
                frodo += 1;
            else if(choices[i] == 5)
                con += 1;
            else if(choices[i] == 6)
                con += 2;
            else if(choices[i] == 7)
                con += 3;
        } // 3
        
        if(survey[i] == "CF"){
            if(choices[i] == 1)
                con += 3;
            else if(choices[i] == 2)
                con += 2;
            else if(choices[i] == 3)
                con += 1;
            else if(choices[i] == 5)
                frodo += 1;
            else if(choices[i] == 6)
                frodo += 2;
            else if(choices[i] == 7)
                frodo += 3;
        }  // 4
        
        if(survey[i] == "MJ"){
            if(choices[i] == 1)
                muzi += 3;
            else if(choices[i] == 2)
                muzi += 2;
            else if(choices[i] == 3)
                muzi += 1;
            else if(choices[i] == 5)
                jayz += 1;
            else if(choices[i] == 6)
                jayz += 2;
            else if(choices[i] == 7)
                jayz += 3;
        } // 5
        
        if(survey[i] == "JM"){
            if(choices[i] == 1)
                jayz += 3;
            else if(choices[i] == 2)
                jayz += 2;
            else if(choices[i] == 3)
                jayz += 1;
            else if(choices[i] == 5)
                muzi += 1;
            else if(choices[i] == 6)
                muzi += 2;
            else if(choices[i] == 7)
                muzi += 3;
        } // 6
        
        if(survey[i] == "AN"){
            if(choices[i] == 1)
                apeach += 3;
            else if(choices[i] == 2)
                apeach += 2;
            else if(choices[i] == 3)
                apeach += 1;
            else if(choices[i] == 5)
                neo += 1;
            else if(choices[i] == 6)
                neo += 2;
            else if(choices[i] == 7)
                neo += 3;
        }  // 7
        
        if(survey[i] == "NA"){
            if(choices[i] == 1)
                neo += 3;
            else if(choices[i] == 2)
                neo += 2;
            else if(choices[i] == 3)
                neo += 1;
            else if(choices[i] == 5)
                apeach += 1;
            else if(choices[i] == 6)
                apeach += 2;
            else if(choices[i] == 7)
                apeach += 3;
        }  // 8
          
    }
    
    if(rion >= tube)
        answer.push_back('R');
    else
        answer.push_back('T');
    
    if(con >= frodo)
        answer.push_back('C');
    else
        answer.push_back('F');
    
    if(jayz >= muzi)
        answer.push_back('J');
    else
        answer.push_back('M');
    
    if(apeach >= neo)
        answer.push_back('A');
    else
        answer.push_back('N');
        
    
    
    return answer;
}
