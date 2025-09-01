#include <stdio.h>

#define MAX_SIZE 100

int maze[MAX_SIZE][MAX_SIZE];
int queue[MAX_SIZE * MAX_SIZE][2];
int row, col;

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

int bfs() {
    int front = 0;
    int rear = 0;
    queue[front][0] = 0;
    queue[front][1] = 0;
    rear++;

    while(front < rear) {
        int x = queue[front][0];
        int y = queue[front][1];
        front++;

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= row || ny < 0 || ny >= col) {
                continue;
            }
            if (maze[nx][ny] == 1) {
                maze[nx][ny] = maze[x][y] + 1;
                queue[rear][0] = nx;
                queue[rear][1] = ny;
                rear++;
            }
        }
    }
    return maze[row-1][col-1];
}

int main() {
    scanf("%d %d", &row, &col);

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            scanf("%1d", &maze[i][j]);
        }
    }

    printf("%d\n", bfs());
}