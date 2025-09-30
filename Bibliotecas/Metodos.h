#ifndef METODOS_H
#define METODOS_H
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h> // Pra Função de Tempo 
#include <math.h>

double Bissec(char funcao[], double Pos_esq, double Pos_dir, double Precisao);
double FalsaPos(char funcao[], double Pos_esq, double Pos_dir, double Precisao);
double NewtonRaphson(char funcao[],double x0, char derivadafx[], double Precisao);
double Secante(char funcao[], double x0, double x1, double Precisao);
double func(double x);

#endif 