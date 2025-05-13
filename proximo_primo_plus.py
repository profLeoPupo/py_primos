import math
import time
from multiprocessing import Pool


# Função para verificar se um número é primo
def is_prime(n):
    """
    Verifica se um número 'n' é primo de forma otimizada.
    A função utiliza alguns truques matemáticos:
    1. Elimina os múltiplos de 2 e 3 rapidamente.
    2. Verifica a primalidade apenas para números ímpares que não são múltiplos de 3.
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:  # Verifica divisibilidade por i e i + 2
            return False
        i += 6
    return True


# Função para gerar todos os números primos até 'n' usando o Crivo de Eratóstenes
def crivo_de_eratostenes(n):
    """
    Gera uma lista de números primos até o número 'n' utilizando o Crivo de Eratóstenes.
    Este método é muito eficiente para encontrar todos os primos em um intervalo grande.
    """
    primos = [True] * (n + 1)  # Assume que todos os números são primos inicialmente
    primos[0], primos[1] = False, False  # 0 e 1 não são primos

    for p in range(2, int(math.sqrt(n)) + 1):
        if primos[p]:
            for i in range(p * p, n + 1, p):  # Marca os múltiplos de p como não primos
                primos[i] = False

    # Retorna uma lista com os números primos
    return [x for x in range(2, n + 1) if primos[x]]


# Função para contar a quantidade de números primos até 'n'
def contar_primos(n):
    """
    Conta a quantidade de números primos até 'n' utilizando o Crivo de Eratóstenes para otimizar.
    """
    primos = crivo_de_eratostenes(n)
    return len(primos)


# Função para encontrar o próximo número primo após 'n'
def proximo_primo(n):
    """
    Encontra o próximo número primo maior que 'n', verificando a primalidade de cada número.
    """
    num = n + 1
    while not is_prime(num):
        num += 1
    return num


# Função para verificar a primalidade em paralelo para acelerar o processo
def verificar_primos_em_paralelo(intervalo):
    """
    Verifica se os números em um intervalo são primos utilizando múltiplos processos.
    Isso distribui a carga de trabalho, utilizando o poder de múltiplos núcleos da CPU.
    """
    with Pool() as pool:
        return pool.map(is_prime, intervalo)


# Função principal que solicita ao usuário o número e executa as operações
def main():
    try:
        # Solicita ao usuário um número para contar os primos e descobrir o próximo
        num = int(input(
            "Digite um número para contar a quantidade de números primos até esse número e descobrir o próximo primo: "))

        # Inicia o tempo para medir o desempenho
        start_time = time.time()

        # Contagem de primos
        quantidade_primos = contar_primos(num)
        print(f"A quantidade de números primos até {num} é: {quantidade_primos}")

        # Encontrando o próximo primo
        proximo = proximo_primo(num)
        print(f"O próximo número primo após {num} é: {proximo}")

        # Medir o tempo total
        end_time = time.time()
        print(f"Tempo de execução: {end_time - start_time:.5f} segundos.")

    # Caso o usuário digite algo que não seja um número
    except ValueError:
        print("Por favor, insira um número válido.")


# Chama a função principal para rodar o programa
if __name__ == "__main__":
    main()
