#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 1000000000

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int case_num;
    int sum[501] = {0, };
    int sol[501][501] = {0, };
    cin >> case_num;

    for(int i = 0; i < case_num; i++) {
        int file_size;
        cin >> file_size;
        for(int j = 0; j < file_size; j++) {
            int tmp;
            cin >> tmp;
            sum[j+1] = sum[j] + tmp; // 누적 합 구하기 
        }
        for(int range = 1; range < file_size; range++) { // 구해야할 범위
            for(int start = 1; start <= file_size - range; start++) {  // 합치는 범위의 시작 지점
                int end = start + range; // 합치는 범위의 끝 지점
                sol[start][end] = MAX; // 해당 범위(start ~ end)를 합치는데 필요한 최소 비용
                for(int k = start; k < end; k++) { // 최소 비용 갱신
                    sol[start][end] = min(sol[start][end], sol[start][k] + sol[k+1][end] + sum[end] - sum[start-1]);
                }
            }
        }
        cout << sol[1][file_size] << endl;
    }
    

    return 0;
}