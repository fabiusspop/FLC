/* Ex1 

%option noyywrap

%{
#include <stdio.h>
%}

%%
[0-3][0-9]\/[0-1][0-9]\/[0-9]{4} {printf("%s is a valid input\n", yytext); }
. { printf("invalid input"); }
%%

int main()
{
    printf("Enter your date: ");
    yylex();
    return 0;
}

*/

/* Ex2 

%option noyywrap

%{
#include <stdio.h>

%}

%%
[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2, } { printf("Valid email address"); }
. { printf("Invalid output"); }
%%

int main()
{
    printf("Enter email address: ");
    yylex();
    return 0;
}

*/

/* Ex3 

%option noyywrap

%{
#include <stdio.h>
int inside = 0;    
%}

%%
"/*" { inside = 1; }
"*/" { inside = 0; }
[^/\n]+ { if(!inside) ECHO; }
\n { if(!inside) ECHO; inside = 0; }
. { if(!inside) ECHO; }
%%

int main(void)
{
    yylex();
    return 0;
}


*/