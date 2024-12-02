#include <stdio.h>
#include <time.h>

// Recursive Fibonacci function
int fibonacci_recursive(int n) {
    if (n <= 1)
        return n;
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

int main() {
    FILE *file = fopen("recursive_results.txt", "w");
    if (!file) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int n = 5; n <= 30; n++) {
        clock_t start = clock();
        fibonacci_recursive(n);
        clock_t end = clock();
        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        fprintf(file, "%d %.6f\n", n, time_taken);
    }

    fclose(file);
    printf("Recursive results saved.\n");
    return 0;
}
