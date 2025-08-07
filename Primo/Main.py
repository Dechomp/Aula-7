def main():

    num = int ( input("Digite um número: ") )

    i = 2

    while num != i and num > 1:
        if num % i == 0:
            break
        i += 1    

    if num == i:
        print("O número ", num, "é primo")
    elif num == 1:
        print("O número 1 não é primo")
    else:
        print("O número ", num, " não é primo pois é divisivel por ", i)

    numero = int (input ("Digite um número: "))


    return 0
main()