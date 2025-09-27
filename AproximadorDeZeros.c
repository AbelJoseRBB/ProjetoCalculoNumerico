#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include "./Bibliotecas/Metodos.h"

#define precisao 0.00001

void menu(int op);
void Chamada1();
void Chamada2();
void Chamada3();
void Chamada4();

int main(){
    int op;

    while(1){
        printf("\nSelecione o metodo que deseja utilzar: \n");
        printf("1 - Bisseccao\n2 - Falsa Posicao\n3 - Newton-Raphson\n4 - Secante\n0 - Sair\n");
        printf("\nMetodo: ");
        scanf("%d", &op);
        printf("\n");
        menu(op);
    }

}

void menu(int op){

    switch (op){
    case 1:
        Chamada1();
        break;
    case 2:
        Chamada2();
        break;
    case 3:
        Chamada3();
        break;
    case 4:
        Chamada4();
        break;
    case 0:
       exit(1);
    default:
        printf("Opcao invalida!\n");
        break;
    }
}

void Chamada1(){
    double a, b;
    printf("Digite o intervalo desejado\n");
    printf("A: ");
    scanf("%lf", &a);
    printf("B: ");
    scanf("%lf", &b);
    printf("\n");

    if(a >= b){
        printf("Valores Invalidos! Tente Novamente");
        Chamada1();
    }else{
        Bissec(NULL, a, b , precisao);
    }
}

void Chamada2(){
    double a, b;

    printf("Digite o intervalo desejado\n");
    printf("A: ");
    scanf("%lf", &a);
    printf("B: ");
    scanf("%lf", &b);
    printf("\n");

    if(a >= b){
        printf("Valores Invalidos! Tente Novamente");
        Chamada2();
    }else{
        FalsaPos(NULL, a, b , precisao);
    }
}

void Chamada3(){
    double x0;

    printf("Digite a estimativa inicial\n");
    printf("x0: ");
    scanf("%lf", &x0);
    printf("\n");

    NewtonRaphson(NULL, x0, NULL, precisao);
}

void Chamada4(){
    double x0, x1;

    printf("Digite as estimativas iniciais");
    printf("x0: ");
    scanf("%lf", &x0);
    printf("x1: ");
    scanf("%lf", &x1);
    printf("\n");

    Secante(NULL, x0, x1, precisao);
}
