def main():
    inicio = int ( input("Inicio do intervalo: "))
    fim =  int ( input("Fim do intervalo: "))

    if inicio == fim:
        
        i = 1
        print("Tabudada do ", inicio)
        while i <= 10:
            print(inicio, "X", i, " =",inicio * i)
            i += 1
    elif inicio < fim:
        while inicio <= fim:

            i = 1

            print("Tabuada do ", inicio)

            while i <= 10:
                print(inicio, "X", i, " =",inicio * i)
                i += 1
            inicio += 1
            print("\n")
    else:
        while inicio >= fim:

            i = 1

            print("Tabuada do", inicio)

            while i <= 10:
                print(inicio, "X", i, " =",inicio * i)
                i += 1
            
            inicio -= 1
            print("\n")



    return 0
main()