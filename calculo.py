'''
Um programa que receba dois números inteiros e mostra o resultado da soma
da multiplicção, da divisão e subtração de um número pelo outro. 
'''
numero_1 = int(input("Informe um Número:"))
numero_2 =  int(input("Informe outro Número:"))
resultado_soma = numero_1 + numero_2
resultado_multiplicação = numero_1 * numero_2
resultado_subtração = numero_1 - numero_2
resultado_divisão = numero_1 // numero_2
if numero_1 < numero_2:
    print(f"Impossivel{resultado_divisão}")
print("A Soma Foi:", resultado_soma, "A Multiplicação Foi:", resultado_multiplicação,
       "A Subtração Foi:", resultado_subtração, "A Divisão Foi:", resultado_divisão)
