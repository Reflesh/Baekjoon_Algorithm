#include <iostream>
using namespace std;
int height, width;
int dp[501][501] = {0, };
int map[501][501] = {0, };

int sol(int x, int y) {
    if(x == height-1 && y == width-1)
        return 1;

    int dx[4] = {-1, 1, 0, 0}; // 방향지정
    int dy[4] = {0, 0, -1, 1};
    if(dp[x][y] == -1) {
        dp[x][y] = 0;
        for(int dir = 0; dir < 4; dir++) {
            int new_x = dx[dir] + x;
            int new_y = dy[dir] + y;
            if(new_x >= 0 && new_x < height && new_y >= 0 && new_y < width) { // 지도 범위 안인가?
                if(map[new_x][new_y] < map[x][y]) // 이동 가능한가?
                    dp[x][y] += sol(new_x, new_y); // 가능하다면 경로 개수를 더해줌
            }
        }
    }
    return dp[x][y];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> height >> width;
    for(int i = 0; i < height; i++) {
        for(int j = 0; j < width; j++) {
            cin >> map[i][j];
            dp[i][j] = -1; // -1로 초기화
        }
    }

    cout << sol(0, 0) << endl;

    return 0;
}