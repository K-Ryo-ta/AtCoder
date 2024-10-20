#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[200009];
    int b[200009];
    bool flag = false;
    int ans = 0;
    int save_hako = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n - 1; i++) {
        cin >> b[i];
    }
    sort(a, a + n, greater<int>());
    sort(b, b + (n - 1), greater<int>());
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < n - 1; i++) {
        cout << b[i] << " ";
    }
    save_hako = b[0];
    for (int i = 0; i < n; i++) {
        if (flag == false) {
            save_hako = b[i];
        }
        if (a[i] > save_hako) {
            save_hako = b[i];
            flag = true;
            ans = a[i];
        } else {
            flag = false;
        }
    }
    if (flag) {
        cout << -1 << endl;
    } else {
        cout << ans << endl;
    }
}
