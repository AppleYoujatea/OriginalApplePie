#include<iostream>
#include<vector>

using namespace std;

int main() {
    
    int five = 0;
    int three = 0;
    
    int n;
    
    cin >> n;
    
    five = n / 5;
    
    for(; five >= 0; five--){
        three = (n - five * 5)/3;
        
        if(five * 5 + three * 3 == n){
            break;
        }
        
    }
    
    if(five * 5 + three * 3 == n){
        cout << five + three;
    }
    else{
        cout << -1;
    }
}
