#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    vector<int> num(30, 0);
    int student_num;
    for(int i = 0; i < 28; i++) {
        cin >> student_num;
        num[student_num-1] = 1;
    }

    for(int i = 0; i < 30; i++) {
        if(num[i] == 0)
            cout << i + 1 << endl;
    }

    return 0;

}