# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
n=int(input("Digite o Número:"))

for T in range(11):
    print(f"{n} x {T} = {n*T}")