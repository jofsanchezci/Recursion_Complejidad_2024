#include <stdio.h>

int fibonacci_iterative(int n) {
    if (n <= 1)
        return n;
    int a = 0, b = 1, temp;
    for (int i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Fibonacci number (Iterative): %d\n", fibonacci_iterative(n));
    return 0;
}
