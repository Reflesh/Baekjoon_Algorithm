#include <iostream>
#include <vector>
using namespace std;

int main() {
    int size, num;
    cin >> size >> num;

    vector<int> basket(size);
    int start_index, end_index, ball_num;
    for(int i = 0; i < num; i++) {
        cin >> start_index >> end_index >> ball_num;
        for(int j = start_index - 1; j < end_index; j++) {
            basket[j] = ball_num; 
            // cout << " j : " << j << ", basket : " << basket[j] << endl;
        }
    }

    for(int i = 0; i < size; i++) {
        cout << basket[i] << " ";
    }

    return 0;

}