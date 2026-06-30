#include <stdio.h>

int main() {
    float a, b;
    char op;

    printf("Enter first number: ");
    scanf("%f", &a);

    printf("Enter second number: ");
    scanf("%f", &b);

    printf("Enter operation (+, -, *, /): ");
    scanf(" %c", &op);

    switch(op) {
        case '+':
            printf("Addition = %.2f\n", a + b);
            break;

        case '-':
            printf("Subtraction = %.2f\n", a - b);
            break;

        case '*':
            printf("Multiplication = %.2f\n", a * b);
            break;

        case '/':
            if(b != 0.0f)
                printf("Division = %.2f\n", a / b);
            else
                printf("Error: Division by zero is not allowed.\n");
            break;

        default:
            printf("Error: Invalid operation.\n");
    }

    return 0;
}