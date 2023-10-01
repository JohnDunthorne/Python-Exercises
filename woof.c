#include <stdio.h>

int main(void)
{
    int woof = 0;
    int input;
    printf("How many times do you want the dog to bark? ");
    scanf("%d", &input);
    for (input; input > woof; woof++)
    {
        printf("woof\n");
    }
}