cmake_minimum_required(VERSION 4.1.0)

# Nome do projeto
project(AproximadorDeZeros C)

message("Compilando Projeto")

# Usar a versão padrão da linguagem C
set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Garante que o executável fique direto na pasta de build
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

add_subdirectory(Bibliotecas)

# Adiciona o executável, incluindo todos os .c necessários
add_executable(AproximadorDeZeros
    AproximadorDeZeros.c
)

target_link_libraries(AproximadorDeZeros Bibliotecas)