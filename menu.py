
def fun_menu(autorização):
    print(">>>>>>>  INTERLEG   <<<<<<<")
    if autorização == 1:
        while True:
            escolha = input("\
                \n1º)CADASTRO DE EMPRESAS \
                \n2º)LANÇAMENTOS DE PRODUTOS \
                \n3º)CONTROLE DE ESTOQUE\n|>>"
            )
            if escolha == "1":
                print("entrou 1")
                import CompanyRegistration
                CompanyRegistration.fun_main(1)
            elif escolha == "2":
                print("entrou 2")
            elif escolha == "3":
                print("entrou 3")
            else:
                print(" Opcão inexistente!!! ")
                continue
            break
    else:
        print("Não autorizado")




