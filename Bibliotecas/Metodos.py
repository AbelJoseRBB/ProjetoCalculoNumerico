# Importa bibliotecas necessárias 
import time 
import sympy as sp
import math

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
    x = x0
    iteracoes = 0
    f_x = abs(float(func.subs(var, x)))

    while f_x > precisao:
        iteracoes += 1

        # Verifica se a derivada é próxima de zero
        df_x = float(derivate.subs(var, x))
        if abs(df_x) < 1e-12:
            raise ValueError(f"Derivada próxima de zero em x = {x:.9f} - O método falhou")

        # Calcula próximo x
        x_new = x - float(func.subs(var, x)) / df_x
        f_new = abs(float(func.subs(var, x_new)))

        print(f"Iteração {iteracoes}: x = {x_new:.9f}, f(x) = {f_new:.9f}")

        # Verifica se o método está divergindo
        if abs(x_new) > 1e10 or abs(x_new - x) > 1e5:
            raise ValueError("O método está divergindo para o infinito")
        if math.isnan(x_new):
            raise ValueError("O método encontrou um valor indeterminado (NaN)")

        # Atualiza x e f_x
        x, f_x = x_new, f_new

        # Verifica limite de iterações
        if iteracoes >= MaxIter:
            raise ValueError("Número máximo de iterações atingido sem convergência")

    precisaoFinal = abs(float(func.subs(var, x)))
    print(f"Convergiu após {iteracoes} iterações: raiz = {x:.9f} | Precisão Final = {precisaoFinal:.12f}")

    return x, iteracoes, precisaoFinal


# ------------------------- MÉTODO DA SECANTE -------------------------
@getTime
def Secante(func, x0, x1, precisao, var):
    iteracoes = 0
    f_x0 = float(func.subs(var, x0))
    f_x1 = float(func.subs(var, x1))
    ultimo_x = x1
    xm = x1

    while abs(f_x1) > precisao:
        iteracoes += 1
        denominador = f_x1 - f_x0

        # Verifica se o denominador é próximo de zero
        if abs(denominador) < 1e-12:
            raise ValueError(f"Denominador próximo de zero - O método falhou na iteração {iteracoes}")

        # Calcula próximo x
        xm = x1 - f_x1 * (x1 - x0) / denominador
        f_xm = float(func.subs(var, xm))

        # Checa divergência ou valores inválidos
        if abs(xm) > 1e10 or abs(xm - ultimo_x) > 1e5:
            raise ValueError("O método está divergindo para o infinito")
        if math.isnan(xm):
            raise ValueError("O método encontrou um valor indeterminado (NaN)")

        print(f"Iteração {iteracoes}: xm = {xm:.9f}, f(xm) = {f_xm:.9f}")

        # Atualiza valores para próxima iteração
        ultimo_x = x1
        x0, f_x0 = x1, f_x1
        x1, f_x1 = xm, f_xm

        # Limite de iterações
        if iteracoes >= MaxIter:
            raise ValueError("Número máximo de iterações atingido sem convergência")

    precisaoFinal = abs(float(func.subs(var, xm)))
    print(f"Convergiu após {iteracoes} iterações: raiz = {xm:.9f} | Precisão Final = {precisaoFinal:.12f}")

    return xm, iteracoes, precisaoFinal