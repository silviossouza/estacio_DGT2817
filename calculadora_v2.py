saida = ''


def adicao(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    if num2 == 0:
        return 'Não foi possível realizar a divisão por 0'
    return num1 / num2


def calculadora(num1, num2, operacao):
    operacao = operacao.lower()

    if operacao == '+' or operacao == 'adicao' or operacao == 'adição':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao' or operacao == 'subtração':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao' or operacao == 'multiplicação':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao' or operacao == 'divisão':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'

    return resultado


while saida.lower() != 'n':
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação (+, -, *, / ou adicao, subtracao, multiplicacao, divisao): ')

    resultado = calculadora(numero1, numero2, operacao)
    print('Resultado da operação: ' + str(resultado))

    saida = input('Deseja continuar? (S/N): ')
