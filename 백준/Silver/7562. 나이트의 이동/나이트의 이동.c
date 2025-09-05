#include <stdio.h>

#define MAX 300

int dx[8] = {-2, -2, -1, -1, 1, 1, 2, 2};
int dy[8] = {1, -1, 2, -2, 2, -2, 1, -1};

int chess[MAX][MAX];
int qx[MAX * MAX];
int qy[MAX * MAX];
int front, rear;
int size, target_x, target_y;

int bfs(int sx, int sy) {
    front = rear = 0;
    qx[rear] = sx;
    qy[rear] = sy;
    rear++;
    chess[sy][sx] = 0;

    while (front < rear) {
        int x = qx[front];
        int y = qy[front];
        front++;

        if (x == target_x && y == target_y) {
            return chess[y][x];
        }

        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < size && ny >= 0 && ny < size && chess[ny][nx] == -1) {
                chess[ny][nx] = chess[y][x] + 1;
                qx[rear] = nx;
                qy[rear] = ny;
                rear++;
            }
        }
    }
    return -1;
}

int main() {
    int Case;
    scanf("%d", &Case);

    while(Case--) {
        int n;
        scanf("%d", &n);
        size = n;

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                chess[i][j] = -1;
            }
        }

        int now_x, now_y;
        scanf("%d %d", &now_x, &now_y);
        scanf("%d %d", &target_x, &target_y);

        printf("%d\n", bfs(now_x, now_y));
    }

    return 0;
}