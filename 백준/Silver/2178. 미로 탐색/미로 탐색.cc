#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <utility>

using namespace std;

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

int bfs(int row, int col, vector<vector<int>>& maze) {
    queue<pair<int, int>> q;

    q.push({0, 0});

    while (!q.empty()) {
        pair<int, int> current = q.front();
        q.pop();

        int x = current.first;
        int y = current.second;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= row || ny < 0 || ny >= col) {
                continue;
            }

            if (maze[nx][ny] == 1) {
                maze[nx][ny] = maze[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    return maze[row-1][col-1];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int row, col;
    cin >> row >> col;

    vector<vector<int>> maze(row, vector<int>(col));

    for (int i = 0; i < row; i++) {
        string row_str;
        cin >> row_str;
        for (int j = 0; j < col; j++) {
            maze[i][j] = row_str[j] - '0';
        }
    }

    cout << bfs(row, col, maze) << endl;

    return 0;
}