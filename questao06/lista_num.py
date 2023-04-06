def main() :
    somatorio=0
    for i in range(0,5):
        num= int(input("Digite um número :"))
        somatorio += num

    print("A soma dos números digitados foi : ",somatorio)
    

if __name__ == "__main__" :
    main()