#include <stdio.h>
#include <conio.h>

int main()
{
    int a = 10;
    int *p = &a;
    printf("Address of a %d \n",&a);
    printf("printing with pointer %d",p);

    return 0;
}
