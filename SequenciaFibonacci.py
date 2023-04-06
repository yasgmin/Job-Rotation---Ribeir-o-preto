#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
#ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
def sequencia_fibonacci(num):
    a, b = 0, 1

    if num == 0 or num == 1:
        return True

    while b <= num:
        if b == num:
            return True
        a, b = b, a + b

    return False

valor_solicitado = 13

if sequencia_fibonacci(valor_solicitado):
    print(f'O número {valor_solicitado} pertence à sequência de Fibonacci.')
else:
    print(f'O número {valor_solicitado} não pertence à sequência de Fibonacci.')
