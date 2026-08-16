#include <string>
#include <vector>

using namespace std;

long long solution(long long n) {
    long long answer = -1;
    long long num = 1;
    
    while(num * num <= n) {
        if(num * num == n) {
            return (num+1) * (num+1);
            break;
        } else {
            num += 1;
        }
    }
    
    return answer;
}