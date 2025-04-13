#Luiz Eduardo Garcia de Siqueira 170981 AlgoBio Lista 3 Ex2
def continuar():
    resposta = input("Continuar (s/n)? ").strip().lower()

    if resposta == 's':
        print("OK, continuando...")
    elif resposta == 'n':
        print("OK, parando...")
    else:
        print("Entrada inválida. Por favor, digite apenas 's' ou 'n'.")

# Executa o script
continuar()