def main():
    num = int ( input("Digite um número: ") )
    divisores = ""
    i = 2
    j = 0
    while num != i and num > 1:
        if num % i == 0:
            divisores += " " + str ( i )
            j += 1
        i += 1

    if j == 0 and num > 1:
        print ("Número primo")
    elif num == 1:
        print("1 não é primo")
    else:
        print ("Não é primo pois é divisivel por ", j, " números a mais e eles são ", divisores)


    return 0
main()