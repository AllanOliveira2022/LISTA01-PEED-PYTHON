def main() :
    numeros = []
    somaPares=0
    for i in range(0,5):
        numeros.append(int(input("Digite um número: ")))
       
    for i in numeros:
        if (i % 2 == 0):
            somaPares += i
    print("A soma dos números pares é: ",somaPares)    

if __name__ == "__main__" :
    main()