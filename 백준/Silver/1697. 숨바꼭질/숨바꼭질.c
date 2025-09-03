#include <stdio.h>

#define MAX 100000

int queue[MAX+1];
int distance[MAX+1];
int front = 0;
int rear = 0;

int bfs(int x, int y) {
    queue[rear++] = x;
    while(front < rear) {
        int idx = queue[front++];
        if(idx == y)
            return distance[idx];

        // python에서 x-1에 해당하는 코드
        int nx1 = idx-1;
        if(nx1 >= 0 && nx1 <= MAX && distance[nx1] == 0) {
            distance[nx1] = distance[idx] + 1;
            queue[rear++] = nx1;
        }

        // python에서 x+1에 해당하는 코드
        int nx2 = idx+1;
        if(nx2 >= 0 && nx2 <= MAX && distance[nx2] == 0) {
            distance[nx2] = distance[idx] + 1;
            queue[rear++] = nx2;
        }

        // python에서 x*2에 해당하는 코드
        int nx3 = idx*2;
        if(nx3 >= 0 && nx3 <= MAX && distance[nx3] == 0) {
            distance[nx3] = distance[idx] + 1;
            queue[rear++] = nx3;
        }
    }
}

int main() {
    int subin, sibling;
    scanf("%d %d", &subin, &sibling);
    printf("%d\n", bfs(subin, sibling));

    return 0;
}