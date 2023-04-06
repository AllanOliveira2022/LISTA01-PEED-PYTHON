def main() :
    numeros = []
    somaImpar = 0

    for i in range(0,5):
        numeros.append(int(input("Digite um número: ")))

    for i in numeros:
        if i % 2 == 0:
            somaImpar += i
    print("A soma dos números ímapres: ",somaImpar)    

if __name__ == "__main__" :
    main()