def main() :
    lista_num=[]
    for i in range(0,5):
        lista_num.append(int(input("Digite um número: ")))

    print("Esses são os números menores que 5: ")
    for i in lista_num:
        if i < 5:
            print(i, end=', ')

if __name__ == "__main__" :
    main()