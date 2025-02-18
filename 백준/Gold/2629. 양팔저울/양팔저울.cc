#include <iostream>
#include <cmath>
using namespace std;
int weight_num, bead_num;
int weight[31] = {0, };
int bead[8] = {0, };
// dp[사용한 추의 개수][무게 차이]
int dp[31][15001] = {0, };

void sol(int num, int wg) {
    if(num > weight_num) // 구슬의 숫자가 더 큰 경우
        return;
    if(dp[num][wg] == 1) // 이미 연산함
        return;
    dp[num][wg] = 1;

    sol(num + 1, wg + weight[num]);         // 추 추가하기
    sol(num + 1, wg);                       // 그대로 진행
    sol(num + 1, abs(wg - weight[num]));    // 반대편에 추 추가(무게빼기)
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> weight_num;
    for(int i = 0; i < weight_num; i++)
        cin >> weight[i];

    cin >> bead_num;
    for(int i = 0; i < bead_num; i++)
        cin >> bead[i];

    sol(0, 0);

    for(int i = 0; i < bead_num; i++) {
        if(bead[i] > 500 * weight_num)
            cout << "N" << " ";
        else if(dp[weight_num][bead[i]] == 1)
            cout << "Y" << " ";
        else
            cout << "N" << " ";
    }

    return 0;
}