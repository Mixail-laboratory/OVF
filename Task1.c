#include <stdio.h>
#include <math.h>

int main(int argc, char **argv) {
    double epsilon = 1;
    while (1 + epsilon / 2 > 1)
        epsilon /= 2;
    printf("eps = %.13a %e\n", epsilon, epsilon);

    while (epsilon / 2 > 0)
        epsilon /= 2;
    printf("min = %.13a %e\n", epsilon, epsilon);

    while (epsilon * 2 < INFINITY)
        epsilon *= 2;
    printf("max = %.13a %e\n", epsilon, epsilon);
    return 0;
}
