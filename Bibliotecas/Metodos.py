# Importa bibliotecas necessárias 
import time 
import sympy as sp

# Define o limite de iterações para evitar loops infinitos 
MaxIter = 100

# Função para medir o tempo de execução e retornar os resultados 
def getTime(funcao):
    def wrapper(*args, **kwargs):
        start = time.time() # Marca o tempo de início
        result, interacoes = funcao(*args, **kwargs) 
        end = time.time() # Marca o tempo de fim 
        tempo = end - start

        # Retorna um dicionário com a raíz, iterações e tempo de exec.  
        return{
            "raiz": float(result),
            "iteracoes": interacoes,
            "tempo": tempo
        }
    return wrapper


# ------------------------- MÉTODO DA BISSECÇÃO -------------------------
@getTime
def Bissec(func, xe, xd, precisao, var):
    iter = 0
    while True:
        iter += 1
        xm = (xe + xd)/2.0
        f_xm = abs(func.subs(var, xm))

        if(func.subs(var, xe) * func.subs(var, xm) > 0):
            xe = xm
        else:
            xd = xm

        print(f"Iteracao {iter} | f(xm) = {f_xm:.6f} | xm = {xm:.6f}")

        if(f_xm <= precisao or iter >= MaxIter):
            print(f"Convergiu apos {iter} iteracoes: raiz = {xm:.9f}")
            return xm, iter


# ------------------------- MÉTODO DA FALSA POSIÇÃO -------------------------
@getTime
def FalsaPos(func, xe, xd, precisao, var):
    iter = 0
    f_xmed = 1
    while f_xmed > precisao and iter < MaxIter:
        iter += 1
        xm = (xe * func.subs(var, xd) - xd * func.subs(var, xe)) / (func.subs(var, xd) - func.subs(var, xe))
        if func.subs(var, xe) * func.subs(var, xd) > 0 :
            xe = xm
        else:
            xd = xm

        f_xmed = abs(func.subs(var, xm))
        print(f"Iteracao {iter} | f(x) = {f_xmed:.6f} | xm = {xm:.6f}")
    print(f"Convergiu apos {iter} iteracoes: raiz = {xm:.9f}")
    return xm, iter


# ------------------------- MÉTODO DE NEWTON-RAPHSON -------------------------
@getTime
def NewtonRaphson(func, derivate, x0, precisao, var):
    iter = 0
    f_xn = 1
    while f_xn > precisao:
        iter += 1
        xn = x0 - func.subs(var, x0) / derivate.subs(var, x0)
        f_xn = abs(func.subs(var, x0))
        print(f"Iteracao {iter} | f(x) = {f_xn:.6f}")
        x0 = xn
    print(f"Convergiu apos {iter} iteracoes: raiz = {xn:.9f}")
    return xn, iter


# ------------------------- MÉTODO DA SECANTE -------------------------
@getTime
def Secante(func, x0, x1, precisao, var):
    iter = 0
    f_xm = 1

    while f_xm > precisao:
        iter += 1
        xm = (x0 * func.subs(var, x1) - x1 * func.subs(var, x0)) / (func.subs(var, x1) - func.subs(var, x0))
        f_xm = abs(func.subs(var, xm))
        x0 = x1
        x1 = xm

        print(f"Iteracao {iter} | f(x) = {f_xm:.6f}")
    print(f"Convergiu apos {iter} iteracoes: raiz = {xm:.9f}")
    return xm, iter

