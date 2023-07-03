#include <string>
#include <vector>

using namespace std;

int answer = 0;

void generateCombinations(vector<int>& nums, vector<int>& currComb, int index){
    if (currComb.size() == 3) {
        int sum = 0;
        for (int num : currComb) {
            sum += num;
        }
        
        if(sum == 0){
            answer++;
        }
        return;
    }
    
    if(index == nums.size()){
        return;
    }
    
    currComb.push_back(nums[index]);
    generateCombinations(nums, currComb, index + 1);
    currComb.pop_back();
    
    generateCombinations(nums, currComb, index + 1);
}


int solution(vector<int> number) {
    
    vector<int> currComb;
    
    generateCombinations(number, currComb, 0);
    
    return answer;
}
