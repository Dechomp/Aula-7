def main():

    num = int ( input("Digite um número: ") )
    divisores = ""
    i = 2
    j = 0
    while num != i and num > 1:
        if num % i == 0:
            divisores += "\n" + str (i)
            j += 1
        i += 1    

    if j == 0 and num > 1:
        print("O número ", num, "é primo")
    elif num == 1 or num == -1:
        print("O número 1 não é primo")
    else:
        print("O número ", num, " não é primo pois é divisivel por ", divisores)
    return 0
main()