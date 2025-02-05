#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int LAN, num;
    cin >> LAN >> num;

    vector<int> LAN_length(LAN);
    for(int i = 0; i < LAN; i++) {
        cin >> LAN_length[i];
    }
    long long start = 1;
    long long end = *max_element(LAN_length.begin(), LAN_length.end());
    while(start <= end) {
        long long mid = (start + end) / 2;
        int cnt = 0;
        for(int i = 0; i < LAN; i++)
            cnt += LAN_length[i] / mid;
        
        if(cnt >= num)
            start = mid + 1;
        else
            end = mid - 1;
    }

    cout << end << endl;

    return 0;
}