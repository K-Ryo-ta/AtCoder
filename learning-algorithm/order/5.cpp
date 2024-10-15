#include <iostream>
using namespace std;

int main() {
    int n;
    int k;
    int l;
    int count = 0;
    cin >> n >> k;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            l = k - i - j;
            if (l >= 1 && l <= n) {
                count++;
            }
        }
    }
    cout << count << endl;
    return 0;
}
