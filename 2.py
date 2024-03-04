def verifica_num(num):
    a = 0
    b = 1
    while b < num:
        aux = b
        b = a + b
        a = aux
    if b == num or num == 0:
        return True
    else:
        return False

num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if verifica_num(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
