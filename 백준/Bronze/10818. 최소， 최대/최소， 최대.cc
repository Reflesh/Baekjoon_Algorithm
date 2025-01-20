#include <iostream>
#include <vector>
using namespace std;

int main() {
    int num;

    cin >> num;

    vector<int> ls(num);
    int max_result = -10000001;
    int min_result = 10000001;

    for(int i = 0; i < num; i++) {
        cin >> ls[i];
    }

    for(int i = 0; i < num; i++) {
        if (ls[i] > max_result) {
            max_result = ls[i];
        }
        if (ls[i] < min_result) {
            min_result = ls[i];
        }
    }

    cout << min_result << " " << max_result << endl;

    return 0;

}