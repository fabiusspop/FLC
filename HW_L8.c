#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    // Ex1 - Search if an  element is in an array

    /*

    int n;
    printf("n = ");
    scanf("%d", &n);

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        printf("arr[%d]= ", i);
        scanf("%d", &arr[i]);
    }

    int searched;
    printf("Enter searched number: ");
    scanf("%d", &searched);

    int found = 0;
    while (found != 1)
    {
        for (int i = 0; i < n; i++)
        {
            if (arr[i] == searched)
                found = 1;
        }
        if (found == 0)
            continue;
    }

    if (found == 1)
    {
        printf("Element was found!");
    }
    else
    {
        printf("Element was not found.");
    }

    return 0;

    */

    // Ex 2 - Add two 2D arrays.

    /*

    int arr1[2][2] = {{1, 2}, {3, 4}};
    int arr2[2][2] = {{5, 6}, {7, 8}};
    int sum[2][2];

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            sum[i][j] = arr1[i][j] + arr2[i][j];
        }
    }

    printf("Sum of the two 2D arrays:\n");

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", sum[i][j]);
        }
        printf("\n");
    }

    return 0;

    */

    // Ex 3 - Check if two 2D arrays are equal.

    /*

    int arr1[2][2] = {{1, 2}, {3, 4}};
    int arr2[2][2] = {{1, 2}, {3, 4}};

    int isEqual = 1;

    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            if (arr1[i][j] != arr2[i][j])
            {
                isEqual = 0;
                break;
            }
        }

        if (isEqual == 0) {
            break;
        }
    }

    if (isEqual == 1)
    {
        printf("The two 2D arrays are equal!");
    }
    else
    {
        printf("The two 2D arrays are not equal.");
    }

    return 0;

    */

    // Ex 4 - Find the length of a string.

    /*

    char str[] = "Hello";

    int l = strlen(str);

    printf("Length of the string is %d",l);

    */

    // Ex 5 - Search for the word FILS and display its index.

    /*

    char ex[] = "FILS is part of UPB. I am a student at FILS. Welcome!";

    char word[] = "FILS";

    char *ptr = strstr(ex, word);

    if (ptr != NULL)
    {
        int index = ptr - ex;

        printf("Word found at index %d.", index);
    }
    else
    {
        printf("Word not found.");
    }

    return 0;

    */

    // Ex 6 - Check if a string is a palindrome.

    char s[20];

    printf("Enter word: ");
    scanf("%s", s);

    int i = 0;
    int j = strlen(s) -1;

    int ok = 1;

    while (i < j)
    {
        if (s[i] != s[j])
        {
            ok = 0;
            break;
        }

        i++;
        j--;
    }

    if (ok == 1)
    {
        printf("String is a palindrome!");
    }
    else
    {
        printf("String is not a palindrome.");
    }

    return 0;

}
