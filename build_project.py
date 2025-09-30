#!/usr/bin/env python3
import os
import subprocess
import sys

# Nome da pasta de build
build_dir = "build"

# Cria a pasta build se não existir
os.makedirs(build_dir, exist_ok=True)

# Detecta o gerador (Ninja se disponível, senão Make)
def detect_generator():
    try:
        subprocess.run(["ninja", "--version"], check=True, stdout=subprocess.DEVNULL)
        return "Ninja"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

generator = detect_generator()
cmake_cmd = ["cmake", "-S", ".", "-B", build_dir]
if generator:
    cmake_cmd += ["-G", generator]

# Roda o CMake
print("Configuring project with CMake...")
subprocess.run(cmake_cmd, check=True)

# Compila o projeto
print("Building project...")
subprocess.run(["cmake", "--build", build_dir], check=True)

print("Build concluído! Executável dentro da pasta 'build/'.")
