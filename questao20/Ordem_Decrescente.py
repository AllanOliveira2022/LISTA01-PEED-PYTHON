def main() :
    numeros = []

    for i in range(0,5):
        numeros.append(int(input("Digite um número: ")))

    print("Aqui está os números em ordem Decrescente: ")
    numeros.sort(key=int,reverse=True)
    print(numeros, end=' ,')

if __name__ == "__main__" :
    main()