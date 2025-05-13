import math


# Função para verificar se um número é primo
def is_prime(n):
    """
    Verifica se um número 'n' é primo.
    Um número é primo se for maior que 1 e não for divisível por nenhum número
    entre 2 e a raiz quadrada de 'n'.
    """
    if n < 2:
        return False  # Qualquer número menor que 2 não é primo
    for i in range(2, int(math.sqrt(n)) + 1):  # Verificação até a raiz quadrada de n
        if n % i == 0:  # Se 'n' for divisível por 'i', não é primo
            return False
    return True  # Se não for divisível por nenhum número, é primo


# Função para contar a quantidade de números primos até 'n'
def contar_primos(n):
    """
    Conta a quantidade de números primos no intervalo [2, n].
    Para isso, percorre todos os números no intervalo e verifica se são primos.
    """
    contador = 0  # Variável para contar os números primos
    for i in range(2, n + 1):  # Percorre todos os números de 2 até 'n'
        if is_prime(i):  # Verifica se o número é primo
            contador += 1  # Se for primo, incrementa o contador
    return contador


# Função para encontrar o próximo número primo após 'n'
def proximo_primo(n):
    """
    Encontra o próximo número primo maior que 'n'.
    A função testa sucessivamente os números maiores que 'n' até encontrar o próximo primo.
    """
    num = n + 1  # Começa a busca a partir de n+1
    while not is_prime(num):  # Continua procurando até encontrar o próximo primo
        num += 1
    return num


# Função principal que solicita ao usuário o número e executa as operações
def main():
    try:
        # Solicita ao usuário um número para contar os primos e descobrir o próximo
        num = int(input(
            "Digite um número para contar a quantidade de números primos até esse número e descobrir o próximo primo: "))

        # Conta a quantidade de números primos até o número informado
        quantidade_primos = contar_primos(num)
        print(f"A quantidade de números primos até {num} é: {quantidade_primos}")

        # Encontra o próximo número primo após o número informado
        proximo = proximo_primo(num)
        print(f"O próximo número primo após {num} é: {proximo}")

    # Caso o usuário digite algo que não seja um número
    except ValueError:
        print("Por favor, insira um número válido.")


# Chama a função principal para rodar o programa
if __name__ == "__main__":
    main()
