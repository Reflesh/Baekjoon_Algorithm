#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int binary_sort(int N, const vector<int>& res) {
    int left_idx = 0;
    int right_idx = res.size() - 1;
    while (left_idx <= right_idx) {
        int mid = (left_idx + right_idx) / 2;
        if (N > res[mid])
            left_idx = mid + 1;
        else if (N < res[mid])
            right_idx = mid - 1;
        else // 값을 찾은 경우
            return 1;
    }
    return 0; // 값을 찾지 못한 경우
}

int main() {
    int num;
    cin >> num;

    vector<int> res(num);
    for (int i = 0; i < num; ++i) {
        scanf("%d", &res[i]);
    }
    sort(res.begin(), res.end());

    int M;
    cin >> M;

    vector<int> cmp(M);
    for (int i = 0; i < M; ++i) {
        scanf("%d", &cmp[i]);
    }

    for (int i = 0; i < M; ++i) {
        printf("%d\n", binary_sort(cmp[i], res));
    }

    return 0;
}