def main() :
    palavras=[]
    for i in range(0,5):
        palavras.append(str(input("Digite uma palavra: ")))
    print("Palavras começadas em 'A':")

    for i in palavras:
        if i[0] == "a":
            print(i,end=' ,')

if __name__ == "__main__" :
    main()