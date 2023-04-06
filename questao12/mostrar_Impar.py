def main() :
    numeros= []
    for i in range(0,5):
        numeros.append(int(input("Digite um número: ")))
    print("Os números ímpares são: ")
    for i in numeros:
        if (i % 2 != 0):
            print("Impar: ",i)


if __name__ == "__main__" :
    main()