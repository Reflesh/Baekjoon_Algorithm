#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int num, standard;
    cin >> num >> standard;
    int card[100] = {0};
    vector<int> max_;

    for(int i = 0; i < num; i++) {
        cin >> card[i];
    }

    for(int i = 0; i < num-2; i++) {
        for(int j = i+1; j < num-1; j++) {
            for(int k = j+1; k < num; k++) {
                int card_sum = card[i] + card[j] + card[k];
                if(card_sum <= standard)
                    max_.push_back(card_sum);
            }
        }
    }

    cout << *max_element(max_.begin(), max_.end()) << endl;

    return 0;
}