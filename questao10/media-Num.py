def main() :
    soma=0
    media=0
    tam=0
    for i in range(0,5):
        numero=(int(input("Digite um número: ")))
        soma += numero
        tam += 1
    media= soma / tam
    print("A média dos números é: ",media)

if __name__ == "__main__" :
    main()