#include <stdio.h>
/*
int main()
{

int year = 2002;

if (year % 4 == 0)
{
    if ((year % 100)!=0 && (year % 400)!=0)
        printf("The year is a leap year.");
    else
        printf("The year is not a leap year.");
}
else
{
    printf("The year is not a leap year.");
}

return 0;

}
*/

/*

int main()
{
    int n = 24;
    
    int c;
    
     if (n < 0)
    {
        c = 0;
    }
    
    if (n == 0)
    {
        c = 1;
    }
    
    if (n > 0)
    {
        c = 2;
    }
    
    switch (c)
    {
        case 0:
            printf("Given number is negative.");
            break;
        
        case 1: 
            printf("Given number is equal to zero.");
            break;
            
        case 2: 
            printf("Given number is positive.");
            break;
        
        default:
            printf("Invalid output.");
    }

    return 0;
}
*/

/*
int main()
{
    int sum = 0;
    int i = 1;
    
    while (i < 20)
    {
        sum += i;
        i += 2;
    }
    
    printf("%i\n", sum);

    return 0;
}
*/

/*
int main()
{
    int n = 123456;
    int d = 0;
    
    while (n != 0)
    {
        d++;
        n/=10;
    }

    printf("%i\n", d);
    
    return 0;
}
*/

/*
int main()
{

    int arr[]={1,2,3,4,5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int sum = 0;
    
    for (int i = 0; i < n; i++)
    {
        sum += arr[i];
    }
    
    printf("%i\n", sum);

    return 0;
}
*/

/*
int main()
{
    int a = 1;
    int b = 2;
    int c = 3;
    
    int max, max1, max2;
    
    if (a > b)
    {
        max1 = a;
    }
    else
    {
        max1 = b;
    }
    
    if (b > c)
    {
        max2 = b;
    }
    else
    {
        max2 = c;
    }
    
    if (max1 > max2)
    {
        max = max1;
    }
    else
    {
        max = max2;
    }
    
    printf("%i\n", max);

    return 0;
}
*/




