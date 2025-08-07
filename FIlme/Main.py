def main():
    idade = int ( input ("Digite a sua idade: "))

    if idade >= 18:
        print("Entrada liberada")
    elif idade >= 16:
        acomp = input ("Vc está acompanhado? ")

        if acomp == "Sim" or acomp == "S" or acomp == "s":
            print("Entrada liberada")
        else:
            print("Entrada proibida")
    else:
        print("Entrada proibida")

    return 0
main()