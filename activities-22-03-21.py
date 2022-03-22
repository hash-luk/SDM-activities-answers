
#1 - Escreva um algoritmo que imprima na tela: Olá Mundo!
from cgitb import reset
from dis import dis
import math
import numbers
from unittest import result


def printHelloWorld():
    print("Hello World")


#2 - Escreva um programa que imprima seu nome na tela.
def printName():
    nome = input("Escreva seu nome: ")
    print(nome)

#3 - O que o código a seguir imprime?

# print("*\n**\n***\n****\n*****")

'''
O código imprime o seguinte resultado:

*
**
***
****
*****
'''

#4 - O que aparece na janela do console, quando cada uma das instruções abaixo são executadas, para: x = 2 e y = 3? Execute cada uma das linhas abaixos e, se necessário, faça os devidos ajustes no código.


def printValues():
    x=2
    y=3

    #a) print(“x = ” + x);
    #print("x = ", x); #Aparecia que apenas podiam ser concatenadas string e não do tipo int.Erro de syntaxe corrigido, aagora o código imprime: x = 2

    #b) print(“O valor de x + x é ” + (x + x));
    #print("O valor de x + x é ", (x + x)); #Aparecia que apenas podiam ser concatenadas string e não do tipo int.Erro de syntaxe corrigido, aagora o código imprime: O valor de x + x é 4

    #c) print(“x = ”);
    #print("x = ",x); #Aparecia no console: SyntaxError: invalid character '“'. Erro de syntaxe corrigido e agora imprime x = 2

    #d) print((x + y) + “ = “ + (y + x)
    print((x + y) , " = "  , (y + x)) #Aparecia: SyntaxError: invalid character '“'. Erro de syntaxe corrigido e agora imprime 5 = 5 


#5 - Escreva um algoritmo que imprima na tela a seguinte mensagem:
def printPhrase():
    print("A programação é aprendida escrevendo programas - Brian Kernighan")

#6 - Crie um algoritmo que imprima o produto entre os números 25 e 27
def multiply2Numbers():
    num1 = 25
    num2 = 27
    result = 25 * 27

    print(f"O produto de 25 * 27 é {result}")


#7 - Crie um algoritmo que imprima a média aritmética entre os números 4, 12, 15.
def arithmeticAverage():
    numbers = [4,2,15]
    sommatory = 0
    result = 0

    for n in numbers:
        sommatory += n

    result = sommatory / len(numbers)

    print(result)

#8 - Faça um programa que leia um número inteiro e mostre-o na tela da seguinte forma:
#O número inteiro digitado foi 4.
def showNumber():
    notANumber = True

    while notANumber:
        userNumber = input("Digite seu número e aperte enter: ")
        boolInput = userNumber.isdigit()

        if boolInput:
            print(f"O número inteiro digitado foi {userNumber}")
            notANumber = False


#9 - Faça um programa que leia e imprima dois números inteiros na tela.
def printTwoNumbers():
    notANumber = True

    while notANumber:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        num1Verify = num1.isdigit()
        num2verify = num2.isdigit()

        if num1Verify or num2verify:
            print(f"O primeiro número foi: {num1} \nO segundo número foi {num2}")
            notANumber = False


#10 - Faça um programa que leia um número inteiro e imprima seu número sucessor e antecessor.
def printPrevNext():
    notANumber = True

    while notANumber:
        num = input("Digite o número: ")

        numVerify = num.isdigit()

        if numVerify:
            prev = int(num) - 1
            prox = int(num) + 1
            print(f"O antecessor é: {prev} \nO sucessor é: {prox}")
            notANumber = False

#11 - Faça um programa que leia o nome, endereço e telefone de um usuário e imprima na tela.
def printUserData():
    name = input("Digite seu nome: ")
    adress = input("Digite seu endereço: ")
    telephone = input("Digite seu telefone: ")

    print(f"O seu nome é {name}\nMora no endereço: {adress}\nPossui o número de telefone: {telephone}")

#12 - Faça um programa que leia e multiplique dois números inteiros.
def multiplyNumbers():
    notANumber = True

    while notANumber:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        num1Verify = num1.isdigit()
        num2verify = num2.isdigit()

        if num1Verify or num2verify:
            result = int(num1) * int(num2)
            print(f"A multiplicação dos números é {result}")
            notANumber = False

#13 - Faça um programa que leia um número real e imprima a terça parte deste número.
def thirdPart():
    notANumber = True

    while notANumber:
        num = input("Digite o número: ")
        numVerify = num.isdigit()

        if numVerify:
            result = int(num) /3
            print(f"A terça parte de {num} é: {result} ")
            notANumber = False

#14 - Faça um programa que leia dois números inteiros e imprima o dividendo, divisor, quociente e resto da divisão
def printDivideEquals():
    notANumber = True

    while notANumber:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        num1Verify = num1.isdigit()
        num2verify = num2.isdigit()

        if num1Verify or num2verify:
            divide = int(num1)/int(num2)
            rest = int(num1)%int(num2)
            print(f"\nO dividendo é: {num1}\nO divisor é: {num2}\nO quoeficiente da divisão é: {divide}\nO resto é: {rest}")
            notANumber = False

#15 - Escreva um programa que solicite do usuário dois números, e imprima o resultado da soma, subtração, multiplicação e divisão.
def equations():
    notANumber = True

    while notANumber:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")
        num1Verify = num1.isdigit()
        num2verify = num2.isdigit()

        if num1Verify or num2verify:
            num1Convert = int(num1)
            num2Convert = int(num2)
            sommatory = num1Convert + num2Convert
            minus = num1Convert - num2Convert
            multiply = num1Convert * num2Convert
            divide = num1Convert / num2Convert
            
            print(f"A soma é: {sommatory}\nA subtração é: {minus}\nA multiplicação é: {multiply}\nA divisão é: {divide}")
            notANumber = False

#16 - Faça um programa que leia quatro números inteiros, calcule e mostre a soma desses números.
def print4Number():
    limiter = 4
    numbers = []

    while limiter > 0:
        numbers.append(input("Digite um número: "))
        limiter -= 1

    for n in numbers:
        print(n)


#17 - Faça um programa que receba três notas, calcule e mostre a média aritmética.
def media():
    limiter = 3
    notas = []
    sommatory = 0

    while limiter > 0:
        notas.append(input("Digite uma nota: "))
        limiter -= 1

    for n in notas:
        sommatory += n 

    media = sommatory/len(notas)

    print(f"A média é: {media}")


#18 - Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.
def ponMedia():
    n1 = input("Digite a primeira nota: ")
    p1 = input("Digite o peso da primeira nota: ")
    n2 = input("Digite a segunda nota: ")
    p2 = input("Digite o peso da segunda nota: ")
    n3 = input("Digite a segunda nota: ")
    p3 = input("Digite o peso da segunda nota: ")

    ponMedia = ((n1*p1) + (n2*p2) + (n3*p3)) / (p1+p2+p3)

    print(f"A média ponderada é {ponMedia}")

#19 - Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.
def calcGains():
    earned = float(input("Digite seu salário (Apenas o valor): R$ "))
    percentage = float(earned) * 0.25
    result = float(earned) + percentage

    print(f"O novo valor é: R$ {result}")

#20 - Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
def percentGains():
    earned = float(input("Digite seu salário (Apenas o valor): R$ "))
    disc = float(input("Digite a parcentagem a calcular(%): "))
    disc = disc * 100
    percentage = float(earned) * disc
    result = int(earned) + percentage

    print(f"O aumento foi de: {disc}\nO novo salário é: {result}")


#21 - Faça um programa que calcule e mostre a área de um triângulo. Sabe-se que
def area():
    base = float(input("Informe a base (Apenas números): "))
    height = float(input("Informe a altura (Apenas números):"))
    area = (base * height) / 2

    print(f"A área do triangulo é: {area}")


#22 - Escreva um programa que receba como entrada o raio de um círculo e imprima o diâmetro, a circunferência e a área. Para isso, utilize as fórmulas: diâmetro = 2r; circunferência = 2πr, área = πr².
def printCircleCalcs():
    r = float(input("Digite o raio: "))
    diameter = r * 2;
    circ = 2 * 3.14 * r
    area = (3.14 *r) ** 2

    print(f"O diâmetro é: {diameter}\nA circunferência é: {circ}\nA área é: {area}")

#23 - Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
def mathCalcs():
    number = 0

    while number <= 0:
        number = float(input("Digite um número maior que 0: "))
        
        if number > 0:
            #o número digitado ao quadrado;
            squareNumber = number ** 2
            #o número digitado ao cubo;
            cubedNumber = number ** 3
            #a raiz quadrada do número digitado.
            sqrtNumber = math.sqrt(number)

            print(f"Número ao quadrado: {squareNumber}\nNúmero ao cubo: {cubedNumber}\nRaiz quadrada do número: {sqrtNumber}")

#24 - Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.
def elevatedNumbers():
    num1 = 0
    num2 = 0

    while num1 <= 0 or num2 <= 0:
        num1 = float(input("Digite o primeiro número maior que 0: "))
        num2 = float(input("Digite o segundo número maior que 0: "))
        
        if num1 > 0 and num2 > 0:
            result = num1 ** num2
            print(f"O número {num1} elevado ao número {num2} é igual a: {result}")

#25 - Sabe-se que: pé = 12 polegadas; 1 jarda = 3 pés e 1 milha = 1,760 jarda. Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
def convertMetrics():
    metric = float(input("Digite a medida em pés (Apenas números): "))

    #polegadas;
    pol = metric * 12

    #jardas;
    jar = round(metric / 3,2)

    #milhas
    mil = round(metric / 5280,5)

    print(f"A conversão para polegadas resulta em: {pol}\nA conversão para jardas resulta em: {jar}\nA conversão para milhas resilta em: {mil}")

#Escreva um programa que receba como entrada um número de 5 dígitos, separe o número em dígitos individuais e os imprima separados por 3 espaços cada um. Por exemplo, se o usuário digitar 42339, o programa deverá imprimir: 4 2 3 3. Dica: utilize as operações de divisão e módulo para extrair cada dígito do número.
def print5DigitsNumber():
    number = ""

    while len(number) < 5:
        number = input("Digite um número com 5 digitos (Apenas números): ")

        if len(number) >= 5:
            for i in range(len(number)):
                print(number[i])
print5DigitsNumber()