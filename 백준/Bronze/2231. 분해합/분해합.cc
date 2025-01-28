#include <iostream>
using namespace std;

int main() {
    int num;
    int result = 0;
    cin >> num;

    for(int i = 1; i < num; i++) {
        int sum = 0;
        int ans = i;
        while(ans != 0) {
            sum += ans % 10;
            ans /= 10;
        }
        if(sum + i == num) {
            result = i;
            break;
        }
    }

    cout << result << endl;

    return 0;
}