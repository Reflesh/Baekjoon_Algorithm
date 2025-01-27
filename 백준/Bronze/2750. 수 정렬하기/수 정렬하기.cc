#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int num;
    cin >> num;
    int number[1000];

    for(int i = 0; i < num; i++) {
        cin >> number[i];
    }

    sort(number, number + num);

    for(int i = 0; i < num; i++) {
        cout << number[i] << endl;
    }

    return 0;
}