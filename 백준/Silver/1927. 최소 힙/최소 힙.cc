#include <iostream>
#include <queue>
using namespace std;

int main() {
    priority_queue<int, vector<int>, greater<int>> heap;
    int cnt;

    cin >> cnt;
    for(int i = 0; i < cnt; i++) {
        int num;
        scanf("%d", &num);
        if(num == 0) {
            if(heap.empty())
                printf("0\n");
            else {
                printf("%d\n", heap.top());
                heap.pop();
            }
        } else {
            heap.push(num);
        }
    }

    return 0;
}