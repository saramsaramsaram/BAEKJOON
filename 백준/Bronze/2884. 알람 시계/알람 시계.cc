#include <stdio.h>

int main() {
    int a,b=0;
    scanf("%d %d", &a, &b);
    b = b - 45;
    if (b<0) {
        a = a - 1;
        b = b + 60;
        if (a<0) {
            a = 23;
        }
    }
    printf("%d %d", a, b);
}