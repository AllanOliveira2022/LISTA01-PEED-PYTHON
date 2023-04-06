def main() :
    numeros = []
    produto = 1
    for i in range(0,5):
        numeros.append(int(input("Digite um número : ")))
        produto = produto * numeros[i]
    
    print("O produto desses números é: ",produto)
if __name__ == "__main__" :
    main()