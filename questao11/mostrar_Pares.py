def main() :
    numeros=[]
    for i in range(0,5):
        numeros.append(int(input("Digite um número: ")))
    print("Este são os números pares: ")
    for i in numeros:
        if i % 2 == 0 :
            print("Par: ",i)
if __name__ == "__main__" :
    main()