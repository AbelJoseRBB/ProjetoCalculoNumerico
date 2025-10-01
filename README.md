# Projeto de zeros de funções
Projeto da disciplina de Cálculo Numerico com objetivo de implementar e 
compreender os métodos iterativos para encontrar zeros de funções.

## Métodos abordados
- Método da Bissecção
- Método da Falsa Posição
- Método de Newton-Raphson
- Método da Secante

## Como Utilizar?
O executável precisa ser compilado a partir do código-fonte disponível no repositório.
Para este caso, recomendamos uma das 3 opções:

1. **Script em Python**

Há um script em Python no código-fonte responsável por automatizar o processo de _build_. Para executá-lo, use a seguinte linha de código no prompt:
```bash
python build_project
```

2. **Através do CMake utilizando Ninja**

É possível compilar através dos comandos de *build* do CMake. Estes são:
```bash
cmake -S . -B build -G Ninja
```
```bash
cmake --build build
```

Note que em ambas as opções acima, são necessários as dependências CMake e Ninja (ou Make em sistemas Unix).
Se você não tiver estas ferramentas na sua máquina, opte pela opção 3:

3. **Compilação através do GCC**

Se você não possuir o CMake e o Ninja para realizar o processo de _build_ do programa, pode optar pelo bom e velho GCC.

Rode a seguinte linha de código no prompt:
```bash
gcc AproximadorDeZeros.c Metodos.c -o AproximadorDeZeros
```

Com a compilação do projeto concluída, basta executar o arquivo **AproximadorDeZeros** gerado na pasta build.