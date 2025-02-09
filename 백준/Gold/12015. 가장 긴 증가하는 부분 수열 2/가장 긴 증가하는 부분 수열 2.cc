#include <iostream>
using namespace std;
#define MAXSIZE 1000001

int binary_search(int start, int end, int target, int res[]) {
    int mid;
    while(start < end) {
        mid = (start + end) / 2;
        if(res[mid] < target)
            start = mid + 1;
        else
            end = mid;
    }
    return end;
}

int main() {
    int size;
    int A[MAXSIZE] = {};
    cin >> size;
    for(int i = 0; i < size; i++)
        cin >> A[i];
    
    int result[MAXSIZE] = {};
    int cnt = 1;
    result[0] = A[0];
    for(int i = 0; i < size; i++) {
        if(result[cnt-1] < A[i]) {
            result[cnt] = A[i];
            cnt++;
        } else {
            int idx = binary_search(0, cnt-1, A[i], result);
            result[idx] = A[i];
        }
    }

    cout << cnt << endl;

    return 0;
}