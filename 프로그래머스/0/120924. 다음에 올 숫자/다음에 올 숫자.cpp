#include <string>
#include <vector>

using namespace std;

int solution(vector<int> common) {
    int answer = 0;
    
    if(common[1] - common[0] == common[2] - common[1]) {
        int d = common[1] - common[0];
        answer = common[common.size() - 1] + d;
    } else {
        int r = common[1] / common[0];
        answer = common[common.size() - 1] * r;
    }
    
    return answer;
}