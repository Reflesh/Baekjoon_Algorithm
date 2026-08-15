#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    if(a > b) {
        while(b <= a) {
            answer += b;
            b++;
        }
    }
    else if(a < b) {
        while(a <= b) {
            answer += a;
            a++;
        }
    } 
    else {
        answer = a;
    }
    return answer;
}