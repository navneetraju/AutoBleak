%{ 
#include<stdio.h> 
#include<string.h> 
int flag=1;
%} 
  
/* Rules Section*/
%% 
"pagePath" {printf("\"pagePath\"");}
"pageviews" {printf("\"pageviews\"");}
"exits" {printf("\"exits\"");}
"nextPageviews" {printf("\"nextPageviews\"");}
"nextExits" {printf("\"nextExits\"");}
"nextPages" {printf("\"nextPages\"");}
"percentExits" {printf("\"percentExits\"");}
"topNextPageProbability" {printf("\"topNextPageProbability\"");}
' {printf("\"");}
\{ {if(flag==1) printf("{"); else printf(",{");}
\[  {printf("[");flag=1;}
\]  {printf("]");flag=0;}
%% 
  
int yywrap(void){} 
  
int main() 
{    
    printf("[");
    yylex(); 
    printf("]");
    return 0; 
} 