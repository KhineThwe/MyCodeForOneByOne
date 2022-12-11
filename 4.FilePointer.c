#include <stdio.h>
#include <conio.h>

int main()
{
    int i=0;
    FILE *fptr;
    char sar[] = "we are myanmar coders\n";
    fptr = fopen("hello.txt","w");

    for(i = 0 ;sar[i] != '\n';i++){
        fputc(sar[i],fptr);
    }
    fclose(fptr);
    return 0;
}
