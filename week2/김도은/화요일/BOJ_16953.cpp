#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
    
    int a, b;
    cin >> a >> b;
    
    queue<int> q;
    bool isFound = false;
    int answer = -1;
    
    q.push(b);
    q.push(-1);
    
    for(int i = 0; i < 40; i++){
        while(q.front() != -1){
            int check = q.front();
            q.pop();
            if(check == a){
                isFound = true;
                answer = i;
                break;
            }
            else{
                if(check / 2 >= a && check %2 == 0){
                    q.push(check / 2);
                }
                
                if((check - 1)/10 >= a && (check -1) % 10 == 0){
                    q.push((check-1)/10);
                }
            }
        }
        
        if(isFound == true){
            break;
        }
        
        q.pop();
        q.push(-1);
        
        if(q.front() < a){
            break;
        }
    }
    
    if(isFound){
        cout << answer +1;
    }
    else{
        cout << -1;
    }
    
    
    
}
