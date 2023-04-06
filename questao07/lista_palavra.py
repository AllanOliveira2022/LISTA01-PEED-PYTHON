def main() :
    palavra = []
    for i in range(0,5):
        palavra.append(str(input("Digite uma palavra: ")))


    maior=str(max(palavra, key=len))# Serve para verificar o tamanho de cada palavra, nesse caso vai pegar a maior
    print("A maior palavra digitada foi: ")
    print(maior)
if __name__ == "__main__" :
    main()