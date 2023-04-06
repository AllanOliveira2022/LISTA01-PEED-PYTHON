def main() :
    Num = []
    for i in range(0,5):
        Num.append(int(input("Digite um número qualquer: ")))

    print("Apenas os números maiores que 10 : ")
    for i in Num:
        if i > 10:
            print("Esse é maior : ",i)    


if __name__ == "__main__" :
    main()