def main() :
    numeros = []
    for i in range(0,5):
        numeros.append(int(input("Digite um número: ")))
    menor= min(numeros) 
    print("O menor número digitado foi: ",menor)   

if __name__ == "__main__" :
    main()