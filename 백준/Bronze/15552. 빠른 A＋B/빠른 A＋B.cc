#include <stdio.h>

int main() {
    int a,i=0;
    int b,c = 0;
    scanf("%d", &a);
    for (i=0; i<a; i++) {
        scanf("%d %d", &b, &c);
        printf("%d\n", b+c);
        
    }
}
    