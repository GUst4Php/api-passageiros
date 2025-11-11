from xmlrpc.client import ServerProxy

def main():

    serv_api = ServerProxy("http://localhost:8000/")

    print("BEM VINDOS AO SISTEMA DE RESERVAS DE VOOS DA GUSTA AIRLINES")

    print("Atividades disponíveis:")
    
    categoria = 10
    

    while categoria != 0:

        print(serv_api.printarTab())
        categoria = int(input("Digite o numero da atvidade que deseja realizar: "))

        if categoria == 1: #atividades relacionadas a reservas
            return None
        
        if categoria == 2: #atividades relacionadas a passageiros
            print("Atividades relacionadas a passageiros:")
            print(serv_api.printarTabPassageiros())
            servicos = int(input("Digite o número do serviço que deseja realizar: "))

            if servicos == 1: #verificar se passageiro existe
                resposta = serv_api.passExiste(int(input("Digite o ID do passageiro que deseja verificar: ")))
                if resposta:
                    print("O passageiro existe no sistema.")
                else:
                    print("O passageiro não existe no sistema.")
                
            if servicos == 2: #consultar passageiro
                resposta = serv_api.getPassageiro(str(input("Digite o ID do passageiro que deseja consultar: ")))
                if resposta:
                    print("Dados do passageiro:")
                    print(resposta)
                else:
                    print("Passageiro não encontrado. Verifique o ID e tente novamente.")

            if servicos == 3: #adicionar passageiro
                resposta = serv_api.adPassageiro(int(input("Digite o ID do passageiro: ")), str(input("Digite o nome do passageiro: ")), str(input("Digite o email do passageiro: ")), str(input("Digite o telefone do passageiro: ")))
                if resposta:
                    print("Passageiro adicionado com sucesso!")
                else:
                    print("Erro ao adicionar passageiro. Verifique os dados e tente novamente.")

            if servicos == 4: #printar tabela de passageiros
                print(serv_api.printarPassageiros())

            if servicos == 5: #sair
                print("Encerrando atividades relacionadas a passageiros.")
                continue

        if categoria == 3:
            print("Atividades relacionadas a Voo:")
            print(serv_api.printarTabVoo())
            servicos = int(input("Digite o número do serviço que deseja realizar: "))
            
            


        if categoria == 5:
            break


            

if __name__ == "__main__":
    main()