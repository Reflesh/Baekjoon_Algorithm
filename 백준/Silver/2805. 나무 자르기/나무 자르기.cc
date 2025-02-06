#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int Tree_num, need_length;
    cin >> Tree_num >> need_length;

    vector<int> Tree(Tree_num);
    for(int i = 0; i < Tree_num; i++) {
        cin >> Tree[i];
    }
    long long start = 1;
    long long end = *max_element(Tree.begin(), Tree.end());
    int result = 0;
    while(start <= end) {
        long long mid = (start + end) / 2;
        long long get_Tree = 0;
        for(int i = 0; i < Tree_num; i++) {
            if(Tree[i] > mid) // 나무가 잘리는 경우
                get_Tree += Tree[i] - mid;
        }
        if(get_Tree >= need_length) {// 더 많은 나무를 가지게 되는 경우
            start = mid + 1;
        }
        else // 목표치보다 더 작은 나무를 가지게 되는 경우         
            end = mid - 1;
    }

    cout << end << endl;

    return 0;
}