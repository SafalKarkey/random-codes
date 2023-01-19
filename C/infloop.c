#include<stdio.h>

int main(){
    int foo;
    while(1){
        printf("Enter foo: ");
        if(scanf("%d", &foo) != 1){
            printf("Cannot take string\n");
            while(getchar() != '\n');
        }
    }
}