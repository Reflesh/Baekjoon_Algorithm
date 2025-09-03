#include <iostream>
#include <queue>
using namespace std;

const int MAX = 100000;
int dis[MAX + 1];

int bfs(int x, int y) {
    queue<int> q;
    q.push(x);

    while (!q.empty()) {
        int idx = q.front();
        q.pop();
        if (idx == y)
            return dis[idx];

        // python에서 x-1에 해당하는 코드
        int nx1 = idx - 1;
        if (nx1 >= 0 && nx1 <= MAX && dis[nx1] == 0) {
            dis[nx1] = dis[idx] + 1;
            q.push(nx1);
        }

        // python에서 x+1에 해당하는 코드
        int nx2 = idx + 1;
        if (nx2 >= 0 && nx2 <= MAX && dis[nx2] == 0) {
            dis[nx2] = dis[idx] + 1;
            q.push(nx2);
        }

        // python에서 x*2에 해당하는 코드
        int nx3 = idx * 2;
        if (nx3 >= 0 && nx3 <= MAX && dis[nx3] == 0) {
            dis[nx3] = dis[idx] + 1;
            q.push(nx3);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int subin, sibling;
    cin >> subin >> sibling;

    cout << bfs(subin, sibling) << endl;

    return 0;
}