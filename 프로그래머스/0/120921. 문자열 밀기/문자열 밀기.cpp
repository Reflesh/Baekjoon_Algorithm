#include <string>
#include <vector>

using namespace std;

int solution(string A, string B) {
    for(int i = 0; i < A.length(); i++) {
        if(A == B) {
            return i;
        }
        
        A = A.back() + A.substr(0, A.length() - 1);
    }
    
    return -1;
}