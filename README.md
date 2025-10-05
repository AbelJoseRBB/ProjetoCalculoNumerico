# 🧮 Projeto de Zeros de Funções  

Projeto desenvolvido para a disciplina de **Cálculo Numérico**, com o objetivo de **implementar e compreender métodos iterativos** utilizados para encontrar zeros de funções.

---

## 🎓 Métodos Abordados  
- 🔹 **Método da Bissecção**  
- 🔹 **Método da Falsa Posição**  
- 🔹 **Método de Newton-Raphson**  
- 🔹 **Método da Secante**

---

## Como Utilizar  

O projeto foi implementado em **Python**.  
A seguir, estão os passos necessários para executá-lo corretamente.

### 📦 Dependências  

Antes de rodar o programa, é necessário instalar algumas dependências.

1. **Python**  
   Como o projeto foi desenvolvido em Python, é essencial que ele esteja instalado em seu sistema.  
   Recomenda-se utilizar a **versão mais recente** da linguagem para evitar incompatibilidades.  
   <br />

2. **Bibliotecas**  
   Foram utilizadas algumas bibliotecas para permitir a interação entre o código e a interface web.  

   📘 A biblioteca **Sympy** é responsável por interpretar a função inserida pelo usuário, além de calcular f(x) e sua respectiva derivada:  
   ```bash
   pip install sympy
   ```

   🌐 Já a biblioteca **Flask** é usada para realizar a comunicação entre a interface web e o backend em Python:  
   ```bash
   pip install flask flask-cors
   ```
   <br />

3. **Extensão do VSCode**  
   💡 Recomendamos a instalação da extensão **Live Server** no VSCode para facilitar a abertura de um servidor local e o uso da interface web.

---

### ▶️ Execução  

Para executar o programa, utilize o seguinte comando no terminal:  

```bash
python Aproximador.py
```

---

## 💻 Funcionamento  

O projeto funciona por meio de uma **interface web interativa**.  
Após executar o arquivo _Aproximador.py_ e iniciar o servidor local com o **Live Server**, o usuário poderá:

1. Inserir a função desejada ✏️  
2. Escolher o método numérico 🔍  
3. Visualizar os resultados em **gráficos comparativos** 📊  

Esses gráficos exibem o **número de iterações** e o **tempo de execução (em milissegundos)** de cada método, facilitando a análise e comparação de desempenho entre eles.

<p align="center">
  <img src="https://github.com/user-attachments/assets/0d3e240f-b72a-4f67-bf7e-9a8aa825c40c">
  <h4 align="center"> Interface Web do Projeto </h4>
</p>

