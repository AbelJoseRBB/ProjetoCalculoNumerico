# Importa bibliotecas necessárias 
import time 
import sympy as sp

# Define o limite de iterações para evitar loops infinitos 
MaxIter = 100

# Função para medir o tempo de execução e retornar os resultados 
def getTime(funcao):
    def wrapper(*args, **kwargs):
        start = time.time() # Marca o tempo de início
        result, interacoes, precisaoFinal = funcao(*args, **kwargs) 
        end = time.time() # Marca o tempo de fim 
        tempo = end - start
    
        # Retorna um dicionário com a raíz, iterações e tempo de exec.  
        return{
            "raiz": float(result),
            "iteracoes": interacoes,
            "tempo": tempo,
            "precisaoFinal": float(precisaoFinal)
        }
    return wrapper


# ------------------------- MÉTODO DA BISSECÇÃO -------------------------
@getTime
def Bissec(func, a, b, precisao, var):
    f_a = float(func.subs(var, a))
    f_b = float(func.subs(var, b))
    
    if f_a * f_b > 0:
        print("Aviso: Não há mudança de sinal no intervalo fornecido.")
        raise ValueError("Não há mudança de sinal no intervalo fornecido.")
    
    iteracoes = 0
    while iteracoes < MaxIter:
        iteracoes += 1
        xm = (a + b) / 2.0
        f_xm = float(func.subs(var, xm))
        
        print(f"Iteração {iteracoes}: xm = {xm:.9f}, f(xm) = {f_xm:.9f}")
        
        # Critério de parada
        if abs(f_xm) <= precisao or abs(b - a)/2 < precisao:
            print(f"Convergência atingida após {iteracoes} iterações.")
            return xm, iteracoes, f_xm
        
        # Atualiza intervalo
        if f_a * f_xm < 0:
            b = xm
            f_b = f_xm
        else:
            a = xm
            f_a = f_xm
    
    print("Atingido número máximo de iterações sem convergência.")
    raise ValueError("Atingido número máximo de iterações sem convergência.")


# ------------------------- MÉTODO DA FALSA POSIÇÃO -------------------------
@getTime
def FalsaPos(func, xe, xd, precisao, var):
    f_xe = float(func.subs(var, xe))
    f_xd = float(func.subs(var, xd))

    if f_xe * f_xd > 0:
        print("Aviso: Não há mudança de sinal no intervalo fornecido.")
        raise ValueError("Não há mudança de sinal no intervalo fornecido.")

    iteracoes = 0
    while iteracoes < MaxIter:
        iteracoes += 1
        # Fórmula da Falsa Posição
        xm = (xe * f_xd - xd * f_xe) / (f_xd - f_xe)
        f_xm = float(func.subs(var, xm))

        print(f"Iteração {iteracoes}: xm = {xm:.9f}, f(xm) = {f_xm:.9f}")

        # Critério de parada
        if abs(f_xm) <= precisao:
            print(f"Convergência atingida após {iteracoes} iterações.")
            return xm, iteracoes, f_xm

        # Atualiza o intervalo
        if f_xe * f_xm < 0:
            xd = xm
            f_xd = f_xm
        else:
            xe = xm
            f_xe = f_xm

    print("Atingido número máximo de iterações sem convergência.")
    raise ValueError("Atingido número máximo de iterações sem convergência.")


# ------------------------- MÉTODO DE NEWTON-RAPHSON -------------------------
@getTime
def NewtonRaphson(func, derivate, x0, precisao, var):
    iter = 0
    f_xn = 1
    
    while f_xn > precisao:
        iter += 1
        # Verifica se a derivada é próxima de zero
        deriv_valor = float(derivate.subs(var, x0))
        if abs(deriv_valor) < 1e-10:
            raise ValueError("Derivada próxima de zero - O método falhou")
            
        xn = x0 - func.subs(var, x0) / deriv_valor
        f_xn = abs(func.subs(var, x0))
        print(f"Iteracao {iter} | f(x) = {f_xn:.6f}")
        x0 = xn
        
        if iter >= MaxIter:
            raise ValueError("Número máximo de iterações atingido")
            
    precisaoFinal = abs(func.subs(var, xn))
    print(f"Convergiu apos {iter} iteracoes: raiz = {xn:.9f} | Precisao Final: {float(precisaoFinal)}")
    return xn, iter, precisaoFinal


# ------------------------- MÉTODO DA SECANTE -------------------------
@getTime
def Secante(func, x0, x1, precisao, var):
    iter = 0
    f_xm = 1

    while f_xm > precisao:
        iter += 1
        denominador = float(func.subs(var, x1) - func.subs(var, x0))
        
        # Verifica se o denominador é próximo de zero
        if abs(denominador) < 1e-10:
            raise ValueError("Denominador próximo de zero - O método falhou")
            
        xm = (x0 * func.subs(var, x1) - x1 * func.subs(var, x0)) / denominador
        f_xm = abs(func.subs(var, xm))
        x0 = x1
        x1 = xm
        
        if iter >= MaxIter:
            raise ValueError("Número máximo de iterações atingido")

        print(f"Iteracao {iter} | f(x) = {f_xm:.6f}")
        
    precisaoFinal = abs(func.subs(var, xm))
    print(f"Convergiu apos {iter} iteracoes: raiz = {xm:.9f} | Precisao Final: {float(precisaoFinal)}")
    return xm, iter, precisaoFinal

