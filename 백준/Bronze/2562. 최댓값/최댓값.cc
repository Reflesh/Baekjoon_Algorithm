#include <iostream>
#include <vector>
using namespace std;

int main() {
    int result_index, num;
    int max_ = 0;

    for(int i = 0; i < 9; i++) {
        cin >> num;
        if (num > max_) {
            max_ = num;
            result_index = i + 1;
        }
    }

    cout << max_ << endl << result_index << endl;

    return 0;

}