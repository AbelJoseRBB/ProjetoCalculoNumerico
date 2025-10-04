import math
import time 
import sympy as sp

x = sp.Symbol('x')
MaxIter = 100

def df(x):
    return math.exp(x) - 3

def getTime(funcao):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = funcao(*args, **kwargs)
        end = time.time()
        print(f"O tempo de execucao foi: {end - start: .6f} segundos")
        return result
    return wrapper

@getTime
def Bissec(func , xe, xd, precisao, x):
    iter = 0
    while True:
        iter += 1
        xm = (xe + xd)/2.0
        f_xm = abs(func.subs(x, xm))

        if(func.subs(x, xe) * func.subs(x, xm) > 0):
            xe = xm
        else:
            xd = xm

        print(f"Iteracao {iter} | f(xm) = {f_xm:.6f} | xm = {xm:.6f}")

        if(f_xm <= precisao or iter >= MaxIter):
            print(f"Convergiu apos {iter} iteracoes: raiz = {xm:.9f}")
            return xm

@getTime
def FalsaPos(func ,xe, xd, precisao, x):
    iter = 0
    f_xmed = 1
    while f_xmed > precisao:
        iter += 1
        xm = (xe * func.subs(x, xd) - xd * func.subs(x, xe)) / (func.subs(x, xd) - func.subs(x, xe))
        if func.subs(x, a) * func.subs(x, b) > 0 :
            xe = xm
        else:
            xd = xm

        f_xmed = abs(func.subs(x, xm))
        print(f"Iteracao {iter} | f(x) = {f_xmed:.6f} | xm = {xm:.6f}")
    print(f"Convergiu apos {iter} iteracoes: raiz = {xm:.9f}")
    return xm

@getTime
def NewtonRaphson(func, derivate, x0, precisao):
    iter = 0
    f_xn = 1
    while f_xn > precisao:
        iter += 1
        xn = x0 - func.subs(x, x0) / derivate.subs(x, x0)
        f_xn = abs(func.subs(x, x0))
        print(f"Iteracao {iter} | f(x) = {f_xn:.6f}")
        x0 = xn
    print(f"Convergiu apos {iter} iteracoes: raiz = {xn:.9f}")
    return xn

@getTime
def Secante(func, x0, x1, precisao):
    iter = 0
    f_xm = 1

    while f_xm > precisao:
        iter += 1
        xm = (x0 * func.subs(x, x1) - x1 * func.subs(x, x0)) / (func.subs(x, x1) - func.subs(x, x0))
        f_xm = abs(func.subs(x, xm))
        x0 = x1
        x1 = xm

        print(f"Iteracao {iter} | f(x) = {f_xm:.6f}")
    print(f"Convergiu apos {iter} iteracoes: raiz = {xm:.9f}")
    return xm

