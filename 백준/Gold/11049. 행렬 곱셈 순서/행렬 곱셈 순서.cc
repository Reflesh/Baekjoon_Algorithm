#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 1000000000

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int case_num;
    cin >> case_num;
    int matrix[502][2];
    int sol[502][502];

    for(int i = 1; i <= case_num; i++)
        cin >> matrix[i][0] >> matrix[i][1];

    for(int len = 1; len < case_num; len++) { // 구간의 범위 -> 곱할 행렬의 개수
        for(int j = 1; len+j <= case_num; j++) { // 연산 시작 지점
            sol[j][len+j] = MAX;
            for(int k = j; k <= len+j; k++) { // 기준점
                sol[j][len+j] = min(sol[j][len+j], sol[j][k] + sol[k+1][len+j] + matrix[j][0] * matrix[k][1] * matrix[len+j][1]);
            }
        }
    }
    
    cout << sol[1][case_num] << endl;

    return 0;
}