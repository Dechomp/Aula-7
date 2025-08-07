def main():
    inicio = int ( input ( "Inicio: "))
    fim = int ( input("Fim: "))
    primos = ""

    if inicio == fim:
        i = 2

        while inicio != i and inicio > 1:
            if inicio % i == 0:
                break
            i += 1
        
        if inicio == i:
            primos += " " + str(inicio)

    elif inicio < fim:
        while inicio <= fim:
            i = 2

            while inicio != i and inicio > 1:
                if inicio % i == 0:
                    break
                i += 1
            
            if inicio == i:
                primos += " " + str (inicio)
            inicio += 1



    else:
        while inicio >= fim:
            i = 2

            while inicio != i and inicio > 1:
                if inicio % i == 0:
                    break
                i += 1
            
            if inicio == i:
                primos += " " + str (inicio)
            inicio -= 1
    
    if primos == "":
        primos = "Intervalo sem primos"

    print("Primos: \n", primos)    
    return 0
main()