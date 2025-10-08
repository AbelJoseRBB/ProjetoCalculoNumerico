# Importas os métodos implementados 
from Bibliotecas.Metodos import Bissec, FalsaPos, NewtonRaphson, Secante

# Importa bibliotecas do Flask para criar a API
from flask import Flask, request, jsonify
from flask_cors import CORS

# Importa a biblioteca Sympy para manipular as funções 
import sympy as sp

# Define a precisão usada nos métodos
PRECISAO = 1e-6

# Cria a aplicação Flask
app = Flask(__name__)

# Permite o acesso à API via WebSite
CORS(app)
    
# ---- ROTA PRINCIPAL DA API -----

# Define a rota que aceita apenas requisões POST
@app.route("/resolver", methods = ["POST"])


def resolver():
    try:
        # Recebe os dados do cliente em formato json
        dados = request.json

        # Recebe a funçao enviada pelo WebSite
        func_str = dados.get("funcao")

        # Conferência para caso o usuário envie uma função 
        if not func_str:
            return jsonify({"erro: Função não informada"}), 400
        
        # Recebe o nome do método selecionado
        metodo = dados.get("metodo")
        
        # Converte a função recebida em uma expressão do Sympy
        func = sp.sympify(func_str)

        # Indentifica a variavel da função enviada
        if len(func.free_symbols) == 0:
            return jsonify({"erro: nenhuma variável encontrada"}), 400
        
        var = list(func.free_symbols)[0]

        # Calcula a derivada da função em relação a variavel obtida 
        derivate = sp.diff(func, var)


        # ----- Faz a chamada do método selecionado --------
        if metodo == "Bissec":
            a = dados.get("a")
            b = dados.get("b")
            result = Bissec(func, a, b, PRECISAO, var)
        elif metodo == "FalsaPos":
            a, b = dados.get("a"), dados.get("b")
            result = FalsaPos(func, a, b, PRECISAO, var)
        elif metodo == "NewtonRaphson":
            x0 = dados.get("x0")
            result = NewtonRaphson(func, derivate, x0, PRECISAO, var)
        elif metodo == "Secante":
            x0 = dados.get("x0")
            x1 = dados.get("x1")
            result = Secante(func, x0, x1, PRECISAO, var)
        else:
            return jsonify({"erro": "Método Inválido"}), 400

        return jsonify({
            "funcao": func_str,
            "metodo": metodo,
            "sucesso": True,
            **result
        })
        
    except ValueError as e:
        return jsonify({
            "sucesso": False,
            "erro": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "sucesso": False,
            "erro": "Erro inesperado: " + str(e)
        }), 400

# Ponto de entrada do app - executa o servidor Flask em modo debug        
if __name__ == "__main__":
    app.run(debug=True) 

