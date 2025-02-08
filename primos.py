import math


# Função para verificar se um número é primo
def is_prime(n):
    # Se o número for menor que 2, não é primo
    if n < 2:
        return False
    # A partir de 2, verificamos se o número é divisível por qualquer número de 2 até a raiz quadrada de n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # Se for divisível, então não é primo
    return True  # Se não for divisível por nenhum, é primo


# Função principal que conta a quantidade de números primos até o número digitado
def contar_primos(n):
    contador = 0  # Variável para contar os números primos
    # Percorre todos os números de 2 até n
    for i in range(2, n + 1):
        if is_prime(i):  # Verifica se o número i é primo
            contador += 1  # Se for primo, incrementa o contador
    return contador  # Retorna o total de números primos


# Função principal que solicita ao usuário o número e executa as operações
def main():
    try:
        # Solicita ao usuário um número para contar os primos
        num = int(input("Digite um número para contar a quantidade de números primos até esse número: "))

        # Conta a quantidade de números primos até o número informado
        quantidade_primos = contar_primos(num)

        # Exibe a quantidade de números primos
        print(f"A quantidade de números primos até {num} é: {quantidade_primos}")

    # Caso o usuário digite algo que não seja um número
    except ValueError:
        print("Por favor, insira um número válido.")


# Chama a função principal para rodar o programa
if __name__ == "__main__":
    main()
