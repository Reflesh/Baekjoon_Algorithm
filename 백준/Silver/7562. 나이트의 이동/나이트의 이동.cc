#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAX = 300;
int dx[8] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[8] = {1, -1, 2, -2, 2, -2, 1, -1};

int bfs(int size, int now_x, int now_y, int target_x, int target_y) {
    vector<vector<int>> chess(size, vector<int>(size, 0));
    queue<pair<int, int>> q;

    q.push({now_x, now_y});
    chess[now_y][now_x] = 0;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        if (x == target_x && y == target_y)
            return chess[y][x];

        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < size && ny >= 0 && ny < size && chess[ny][nx] == 0) {
                chess[ny][nx] = chess[y][x] + 1;
                q.push({nx, ny});
            }
        }
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int size, now_x, now_y, target_x, target_y;
        cin >> size;
        cin >> now_x >> now_y;
        cin >> target_x >> target_y;

        cout << bfs(size, now_x, now_y, target_x, target_y) << "\n";
    }

    return 0;
}