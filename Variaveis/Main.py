def main():
    nome = input("Digite o seu nome: ")
    idade = int (input("Digite a sua idade: "))
    peso = float (input("Digite o seu peso: "))
    isEmpregado = input("Vc possui um emprego? ") 

    print("O ", nome, " tem ", idade, " anos de idade, pesa ",peso)

    if isEmpregado == "Sim":
        print("Ele possui um emprego")
    else:
        print("Ele não possui emprego")
     
    return 0
main()