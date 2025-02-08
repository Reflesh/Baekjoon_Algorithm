#include <iostream>
using namespace std;

int main() {
    int size, find_num;
    cin >> size >> find_num;

    int start = 1;
    int end = find_num;
    int result = 0;
    while(start <= end) {
        int mid = (start + end) / 2;
        int cnt = 0;
        for(int i = 1; i <= size; i++)
            cnt += min(size, mid / i);
        if (cnt < find_num)
            start = mid + 1;
        else {
            result = mid;
            end = mid - 1;
        }
    }
    
    cout << result << endl;

    return 0;
}