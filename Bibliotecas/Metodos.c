#include "Metodos.h"


double func(double x){
    double fun;
    fun = exp(x) - 3*x;
    return fun;
}

double df(double x){

    float deriv;
	deriv = exp(x) - 3;
	return(deriv);


}


double Bissec(char funcao[], double Pos_esq, double Pos_dir, double Precisao){
    int iter = 0;
    double raiz, xmed, F_xmed;

    do {
        iter++;
        xmed = (Pos_esq + Pos_dir) / 2.0;   // força divisão real
        F_xmed = fabs(func(xmed));

        if (func(Pos_esq) * func(xmed) > 0)
            Pos_esq = xmed;
        else
            Pos_dir = xmed;

        printf("Iteracao: %d | f(xm) = %.6f | xm = %.6f\n", iter, F_xmed, xmed);

    } while (F_xmed > Precisao);

    raiz = xmed;
    printf("Convergiu apos %d iteracoes: raiz = %.9f\n", iter, raiz);

    return raiz;
    
}

double FalsaPos(char funcao[], double Pos_esq, double Pos_dir, double Precisao){
    int iter = 0;
    double raiz, xmed, F_xmed = 1, erro;

    while(F_xmed > Precisao){
        iter++;

        xmed = (Pos_esq * func(Pos_dir) - Pos_dir * func(Pos_esq)) / (func(Pos_dir) - func(Pos_esq));

        if(func(Pos_esq) * func(Pos_dir) > 0)
            Pos_esq = xmed;
        else
            Pos_dir = xmed;

        F_xmed = fabs(func(xmed));

        printf("Iteracao: %5d f(x): %10.6lf xm= %10.6lf\n", iter, F_xmed, xmed);
    }
    raiz = xmed;
    
    
    printf("Convergiu apos %4d iteracoes para a raiz = %10.9lf\n", iter, raiz);
    
    return raiz;
}


double NewtonRaphson(char funcao[], double x0, char derivadafx[], double Precisao){
    int iter = 0;
    double xn, F_xn = 1, raiz;

    while(F_xn > Precisao){
        iter++;
        
        xn = x0 - func(x0) / df(x0);
        F_xn = fabs(func(x0));
        printf("Iteracao %d   |f(x)|: %10.6lf\n", iter, F_xn);  /* Imprime o numero da iteracao e o erro */
		x0 = xn;
    }
    
    raiz = xn;
    printf("Convergiu apos %5d iteracoes para a raiz = %10.6lf\n", iter, raiz);

    return raiz;
}

double Secante(char funcao[], double x0, double x1, double Precisao){
    int iter = 0;
    double fxm = 1.0, xMedio, raiz;

    while (fxm > Precisao){
       iter++;
       
       xMedio = (x0 * func(x1) - x1 * func(x0)) / (func(x1) - func(x0));

       fxm = fabs(func(xMedio));
        x0 = x1;
        x1 = xMedio;
        
        printf("Iteracao %5d	f(x): %10.6lf\n", iter, fxm);
    }
    
    raiz = xMedio;
    printf("Convergiu apos %4d iteracoes para a raiz = %10.6lf\n", iter, raiz);
    
    return raiz;
}