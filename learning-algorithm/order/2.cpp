#include <iostream>
using namespace std;

int main() {
    int n;
    int x;
    int a[100];
    cin >> n >> x;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        if (a[i] == x) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}
