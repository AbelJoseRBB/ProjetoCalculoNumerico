# Projeto de zeros de funções
Projeto da disciplina de Cálculo Numerico com objetivo de implementar e 
compreender os métodos iterativos para encontrar zeros de funções.

## Métodos abordados
- Método da Bissecção
- Método da Falsa Posição
- Método de Newton-Raphson
- Método da Secante

## Como Utilizar?
O projeto foi implementado por meio da linguagem de programação Python. A seguir, estão os passos para executar o programa.

### Dependências
Antes de rodar o programa, é preciso baixar algumas dependências para que o código possa ser executado corretamente.

1. **Python**

Claro que, como o projeto é implementado em Python, é necessário que o Python esteja instalado no seu sistema. Recomendamos a última versão da linguagem, para evitar qualquer tipo de erro.
<br />

2. **Bibliotecas**

No nosso projeto, utilizamos algumas bibliotecas para permitir o uso interativo do programa. Primeiro, a biblioteca _sympy_ é responsável por receber o input da função do usuário e permite o cálculo de _f(x)_ e de sua respectiva derivada. 

```bash
pip install sympy
```

Também temos a biblioteca _flask_ que utilizamos para realizar a comunicação entre a interface web e o backend em python

```bash
pip install flask flask-cors
```
<br />

3. **Extensão do VSCode**

Por fim, recomendamos a instalação da extensão **Live Server** do VSCode para facilitar a abertura de um servidor local.

### Execução
Para rodar o programa, execute a seguinte linha no terminal:
```bash
python Aproximador.py
```

## Funcionamento
O projeto funciona a partir da interface web, após a execução do arquivo _Aproximador.py_ e a abertura do servidor local a partir do extensão _Live Server_, o usuário interage com a página inserindo a função que deseja achar alguma raíz e selecionando o método desejado. Com isso, um gráfico será exibido com o número de iterações e também com tempo de execução de cada método, o que facilita a comparação de resultados entre eles.
