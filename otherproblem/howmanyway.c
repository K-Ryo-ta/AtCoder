#include <stdio.h>
int main() {
    long i, j, k;
    long a, b;
    long count = 0;

    while (!(a == 2 || (a == 0 && b == 0))) {
        scanf("%ld %ld", &a, &b);
        for (i = 1; i < a + 1; i++) {
            for (j = 1; j < i; j++) {
                for (k = 1; k < j; k++) {
                    if (i + k + j == b) {
                        count++;
                    }
                }
            }
        }
        if (!(a == 2 || (a == 0 && b == 0))) {
            printf("%ld\n", count);
            count = 0;
        } else {
            return 0;
        }
    }
}
