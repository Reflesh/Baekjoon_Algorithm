#include <iostream>
#include <vector>
using namespace std;

vector<vector<long long>> mul(const vector<vector<long long>> &a, const vector<vector<long long>> &b, int size) {
    vector<vector<long long>> res(size, vector<long long>(size, 0));
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            for (int k = 0; k < size; k++) {
                res[i][j] += a[i][k] * b[k][j];
                res[i][j] %= 1000;  // 문제 조건
            }
        }
    }
    return res;
}

vector<vector<long long>> sol(const vector<vector<long long>> &x, long long n, int size) {
    if (n == 1) {
        vector<vector<long long>> res = x;
        for (int i = 0; i < size; i++)
            for (int j = 0; j < size; j++)
                res[i][j] %= 1000;  // 1000으로 나누기
        return res;
    }

    vector<vector<long long>> tmp = sol(x, n / 2, size);
    tmp = mul(tmp, tmp, size);
    
    if (n % 2 == 1)  // n이 홀수인 경우
        return mul(tmp, x, size);
    return tmp;
}

int main() {
    int size;
    long long pow_num;
    cin >> size >> pow_num;
    vector<vector<long long>> A(size, vector<long long>(size));
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            cin >> A[i][j];
        }
    }

    vector<vector<long long>> result = sol(A, pow_num, size);

    for (const auto& row : result) {
        for (const auto& elem : row) {
            cout << elem << ' ';
        }
        cout << endl;
    }

    return 0;
}