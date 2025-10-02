from Bibliotecas.Metodos import Bissec, FalsaPos, NewtonRaphson, Secante
import sympy as sp

PRECISAO = 1e-6
x = sp.Symbol('x')

def menu():
    while  True:
        print("\nDigite a funcao desejada: ")
        func_str = str(input("Funcao: "))
        func = sp.sympify(func_str)
        derivate = sp.diff(func, x)

        print("\nSelecione o metodo que deseja utilizar:")
        print("1 - Bisseccao")
        print("2 - Falsa Posicao")
        print("3 - Newton-Raphson")
        print("4 - Secante")
        print("0 - Sair")

        op = int(input("\n Selecione um Metodo: "))

        if op == 1:
            a = float(input("A: "))
            b = float(input("B: "))
            Bissec(func,a, b, PRECISAO)
        elif op == 2:
            a = float(input("A: "))
            b = float(input("B: "))
            FalsaPos(func, a, b, PRECISAO)
        elif op == 3:
            x0 = float(input("x0: "))
            NewtonRaphson(func, derivate, x0, PRECISAO)
        elif op == 4:
            x0 = float(input("x0: "))
            x1 = float(input("x1: "))
            Secante(func, x0, x1, PRECISAO)
        elif op == 0:
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()  

