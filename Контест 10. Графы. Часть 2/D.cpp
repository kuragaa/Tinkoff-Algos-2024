#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n;
    cin >> n;
    vector<int> attack(n);
    vector<int> defense(n);
    for(int i = 0; i < n; i++) {
        cin >> attack[i];
    }
    for(int i = 0; i < n; i++) {
        cin >> defense[i];
    }
    vector<int> left{-1};
    vector<int> right;
    set<int> alive;
    for (int i = 0; i < n - 1; i++) {
        left.push_back(i);
    }
    for (int i = 1; i < n; i++) {
        right.push_back(i);
    }
    right.push_back(-1);
    for (int i = 0; i < n; i++) {
        alive.insert(i);
    }
    for (int i = 0; i < n; i++){
        int count = 0;
        set<int> losers;
        for (int m : alive) {
            int dmg = 0;
            if (left[m] != -1){
                dmg += attack[left[m]];
            }
            if (right[m] != -1){
                dmg += attack[right[m]];
            }
            if (dmg > defense[m]){
                losers.insert(m);
                count ++;
            }
        }
        cout << count << ' ';
        alive.clear();
        for (int m : losers) {
            if (left[m] != -1) {
                right[left[m]] = right[m];
                if (losers.find(left[m]) == losers.end()){
                    alive.insert(left[m]);
                }
            }
            if (right[m] != -1) {
                left[right[m]] = left[m];
                if (losers.find(right[m]) == losers.end()){
                    alive.insert(right[m]);
                }
            }
        }
    }

    return 0;
}