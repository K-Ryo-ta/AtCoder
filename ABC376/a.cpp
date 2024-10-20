#include <iostream>
using namespace std;
int main() {
    int n;
    int c;
    cin >> n >> c;
    int T[1009];
    int save_time = 0;
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        cin >> T[i];
    }
    save_time = T[1];
    for (int i = 2; i <= n; i++) {
        if (T[i] - save_time >= c) {
            ans += 1;
            save_time = T[i];
        }
    }
    cout << ans + 1 << endl;
    return 0;
}
