#include <iostream>
#include <vector>
using namespace std;

int main() {
    int row_size_A, col_size_A;
    cin >> row_size_A >> col_size_A;

    // 첫 번째 행렬 입력
    vector<vector<int>> A(row_size_A, vector<int>(col_size_A));
    for (int i = 0; i < row_size_A; i++) {
        for (int j = 0; j < col_size_A; j++) {
            cin >> A[i][j];
        }
    }

    int row_size_B, col_size_B;
    cin >> row_size_B >> col_size_B;

    // 두 번째 행렬 입력
    vector<vector<int>> B(row_size_B, vector<int>(col_size_B));
    for (int i = 0; i < row_size_B; i++) {
        for (int j = 0; j < col_size_B; j++) {
            cin >> B[i][j];
        }
    }

    // 결과값 저장 
    vector<vector<int>> result(row_size_A, vector<int>(col_size_B, 0));
    for (int i = 0; i < row_size_A; i++) {
        for (int j = 0; j < col_size_B; j++) {
            for (int k = 0; k < col_size_A; k++) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    // 결과 출력
    for (int i = 0; i < row_size_A; i++) {
        for (int j = 0; j < col_size_B; j++) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}