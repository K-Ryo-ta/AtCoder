#include <iostream>
using namespace std;

int main() {
    int d, n;
    cin >> d;
    cin >> n;
    int l[100009];
    int r[100009];
    int b[100009];
    int ans[100009];
    for (int i = 1; i <= n; i++) {
        cin >> l[i] >> r[i];
    }
    // 前日比を計算
    for (int i = 1; i <= n; i++) {
        b[l[i]] += 1;
        b[r[i] + 1] -= 1;
    }

    // 累積和を計算
    ans[0] = 0;
    for (int i = 1; i <= d; i++) {
        ans[i] = ans[i - 1] + b[i];
    }

    // 答えを出力
    for (int i = 1; i <= d; i++) {
        cout << ans[i] << endl;
    }

    return 0;
}
