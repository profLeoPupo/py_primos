
---

# Calculadora de Números Primos em Python

Este repositório contém um projeto didático para explorar algoritmos de verificação de números primos, com foco em otimizações matemáticas e técnicas computacionais. O código está organizado em três scripts (primos.py, proximo_primo.py e proximo_primo_plus.py), representando diferentes níveis de implementação.


---

# Sumário

Introdução

Estrutura do Projeto

Explicação dos Algoritmos

Exemplos de Uso

Comparação de Desempenho

Possíveis Melhorias

Como Contribuir



---

## Introdução

Este projeto tem como objetivos:
✅ Demonstrar diferentes abordagens para verificar números primos.
✅ Explorar a complexidade algorítmica e otimizações computacionais.
✅ Servir como material educativo para programação e matemática.


---

## Estrutura do Projeto

📂 Raiz do Repositório

📄 primos.py → Implementação básica com verificação direta.

📄 proximo_primo.py → Algoritmo aprimorado para encontrar o próximo primo.

📄 proximo_primo_plus.py → Implementação otimizada com paralelismo e Crivo de Eratóstenes.

📄 README.md → Documentação detalhada do projeto.



---

## Explicação dos Algoritmos

1️⃣ Implementação Básica (primos.py)

Código inicial utilizando a abordagem ingênua:

def n_primo(n):
    """Verifica se um número é primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

🔹 Complexidade: O(n√n) → Ineficiente para grandes valores.


---

2️⃣ Algoritmo Melhorado (proximo_primo.py)

Usa regras matemáticas para evitar verificações desnecessárias:

def proximo_primo(n):
    """Encontra o próximo número primo maior que 'n'."""
    num = n + 1
    while not n_primo(num):
        num += 2  # Pulando números pares
    return num

🔹 Otimização: Redução de verificações ao eliminar múltiplos de 2 e 3.


---

3️⃣ Algoritmo Avançado (proximo_primo_plus.py)

Crivo de Eratóstenes e paralelismo para acelerar cálculos:

from multiprocessing import Pool

def crivo_de_eratostenes(n):
    """Retorna todos os primos até 'n' usando o Crivo de Eratóstenes."""
    primos = [True] * (n + 1)
    primos[0], primos[1] = False, False
    for p in range(2, int(n ** 0.5) + 1):
        if primos[p]:
            for i in range(p * p, n + 1, p):
                primos[i] = False
    return [x for x in range(2, n + 1) if primos[x]]

def verificar_primos_em_paralelo(intervalo):
    """Utiliza múltiplos núcleos da CPU para verificar primos."""
    with Pool() as pool:
        return pool.map(n_primo, intervalo)

🔹 Complexidade: O(n log log n) → Muito mais rápido para grandes valores.


---

## Exemplos de Uso

Rodando os scripts:

Execute no terminal:

python primos.py  
python proximo_primo.py  
python proximo_primo_plus.py

Saída esperada:

Digite um número: 20
Primos até 20: 8  # (2, 3, 5, 7, 11, 13, 17, 19)

Próximo primo após 20: 23

Crivo de Eratóstenes até 50:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


---

## Comparação de Desempenho

📌 Conclusão: O Crivo de Eratóstenes combinado com paralelismo é a melhor abordagem para grandes intervalos.


---

## Possíveis Melhorias

🚀 Implementar Crivo Segmentado para números acima de 10¹⁰.
📡 Criar uma API REST para verificação de primos.
🖥️ Adicionar uma interface gráfica para visualização dos cálculos.


---

## Como Contribuir

💡 Sinta-se à vontade para abrir uma issue ou enviar um pull request!
📜 Este projeto é aberto para aprimoramentos e otimizações.


---

🔗 ## Referências:

Crivo de Eratóstenes – Wikipedia

Números Primos – Khan Academy


📌 Mantenedor: @profLeoPupo – GitHub


---

Com esse README, seu projeto terá uma excelente apresentação para estudantes, desenvolvedores e possíveis contribuintes. Ele explica a lógica de cada script, os conceitos matemáticos e otimizações, além de fornecer exemplos e métricas de desempenho.

Se precisar de ajustes ou quiser adicionar imagens/tabelas extras, me avise!

