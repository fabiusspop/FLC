/* Ex1
%{
    #include <stdio.h>
%}

%option noyywrap

%%

^(http|https):\/\/[a-zA-Z0-9./-]+[.][a-zA_Z0-9./-]+$ { printf("VALID URL: %s\n", yytext); }
. { printf("NOT a valid URL:%s\n", yytext); 
}

%%

int main(){
    yylex();
    return 0;
}
*/

/* Ex2
%{
    #include <stdio.h>
    int line = 1;
%}

%option noyywrap

%%
\n { printf("%d: ", line++); putchar(yytext[0]); }
. { ECHO; }
%%

int main(void){
    printf("Line number 1: ");
    yylex();
    return 0;
}
*/

/* Ex3

%{
    #include <stdio.h>
}

%option noyywrap

%%

mere { printf("marlboroRosu"); }
.|\n { ECHO; }

%%

int main(void){
    yylex();
    return 0;
}

*/