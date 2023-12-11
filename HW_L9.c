/* EX-1

%{
#undef yywrap
#define yywrap() 1
%}

%option noyywrap

%%
[\n]{
    printf("Hello World!\n");
}
%%

int main()
{
    yylex();
}

*/

/* EX-2

%{
    #include <stdio.h>
}

%%
[aeiouAEIOU] { printf("%s is a vowel\n", yytext); }
. { }
%%

int main(){
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}
*/

/* EX-3 
%{
    #include <stdio.h>
%}

%option noyywrap

%%
I|you|he|she|it|we|you|they { printf("%s is a pronoun\n", yytext); }
[0-9] { printf("%s is a digit\n", yytext); }
%%

int main(){
    yylex();
    return 0;
}
*/

