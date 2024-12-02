#include <stdio.h>
#include <time.h>

// Iterative Fibonacci function
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
    FILE *file = fopen("iterative_results.txt", "w");
    if (!file) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int n = 5; n <= 30; n++) {
        clock_t start = clock();
        fibonacci_iterative(n);
        clock_t end = clock();
        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        fprintf(file, "%d %.6f\n", n, time_taken);
    }

    fclose(file);
    printf("Iterative results saved.\n");
    return 0;
}
