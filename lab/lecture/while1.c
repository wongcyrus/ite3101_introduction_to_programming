#include <stdio.h>

int main(
    int argc,
    char **argv
    ) 
    {
        int number = 1;
        while ( number <= 10 )
        {
            printf("%d\n", number);
            number += 1;
        }
        printf("Done!\n");
        return 0;
    }
