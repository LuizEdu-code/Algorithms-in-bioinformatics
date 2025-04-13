#Luiz Eduardo Garcia de Siqueira 170981 AlgoBio Lista 3 Ex1
def tipo_solucao_if(ph):
    if ph < 0 or ph > 14:
        print("Valor de pH inválido. Deve estar entre 0 e 14.")
    elif ph < 7:
        print("A solução é ácida.")
    elif ph == 7:
        print("A solução é neutra.")
    else:
        print("A solução é básica.")

def tipo_solucao_match(ph):
    match ph:
        case _ if ph < 0 or ph > 14:
            print("Valor de pH inválido. Deve estar entre 0 e 14.")
        case _ if ph < 7:
            print("A solução é ácida.")
        case 7:
            print("A solução é neutra.")
        case _:
            print("A solução é básica.")

def main():
    try:
        ph = float(input("Digite o valor de pH da solução (0 a 14): "))
        print("Escolha o método:")
        print("1 - Usar if-else")
        print("2 - Usar match-case (Python 3.10+)")
        metodo = input("Digite 1 ou 2: ")

        if metodo == "1":
            tipo_solucao_if(ph)
        elif metodo == "2":
            tipo_solucao_match(ph)
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
