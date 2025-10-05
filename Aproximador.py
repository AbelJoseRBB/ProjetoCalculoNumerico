from Bibliotecas.Metodos import Bissec, FalsaPos, NewtonRaphson, Secante
from flask import Flask, request, jsonify
from flask_cors import CORS
import sympy as sp

PRECISAO = 1e-6

app = Flask(__name__)
CORS(app)
    
# ---- API -----
@app.route("/resolver", methods = ["POST"])

def resolver():
    dados = request.json

    # Recebe a funçao enviada pelo WebSite
    func_str = dados.get("funcao")

    if not func_str:
        return jsonify({"erro: Função não informada"}), 400
    
    metodo = dados.get("metodo")
    precisao = dados.get("precisao", PRECISAO)

    func = sp.sympify(func_str)

    # Indentifica a variavel da função enviada
    if len(func.free_symbols) == 0:
        return jsonify({"erro: nenhuma variável encontrada"}), 400
    
    var = list(func.free_symbols)[0]

    # Calcula a derivada da função em relação a variavel obtida 
    derivate = sp.diff(func, var)

    if metodo == "Bissec":
        a = dados.get("a")
        b = dados.get("b")
        result = Bissec(func, a, b, precisao, var)
    elif metodo == "FalsaPos":
        a, b = dados.get("a"), dados.get("b")
        result = FalsaPos(func, a, b, precisao, var)
    elif metodo == "NewtonRaphson":
        x0 = dados.get("x0")
        result = NewtonRaphson(func, derivate, x0, precisao, var)
    elif metodo == "Secante":
        x0 = dados.get("x0")
        x1 = dados.get("x1")
        result = Secante(func, x0, x1, precisao, var)
    else:
        return jsonify({"erro: Método Inválido"}), 400
    
    return jsonify({
        "funcao": func_str,
        "metodo": metodo,
        **result
    })
        
if __name__ == "__main__":
    app.run(debug=True) 

