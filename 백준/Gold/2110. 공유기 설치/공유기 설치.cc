#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int house_num, router;
    cin >> house_num >> router;

    vector<int> house(house_num);
    for(int i = 0; i < house_num; i++)
        cin >> house[i];
    
    sort(house.begin(), house.end());

    int start = 1; // 최소 거리
    int end = house[house_num-1] - house[0]; // 최대 거리
    int result = 0;
    while (start <= end) {
        int mid = (start + end) / 2;
        int cnt = 1;
        int prev_house = house[0]; // 이전 설치 위치
        for(int i = 1; i < house_num; i++) {
            if(house[i] - prev_house >= mid) {
                cnt++;
                prev_house = house[i]; // 설치 위치 갱신
            }
        }
        if(cnt >= router) {
            result = mid;
            start = mid + 1;
        }
        else
            end = mid - 1;
    }

    cout << result << endl;

    return 0;
}